#!/usr/bin/env python

import asyncio
import csv
import logging
from pprint import pprint

import aiohttp
import click
import pendulum
from neo4j import GraphDatabase
from smart_open import open

BACKEND_URI = "http://localhost:3000"


tasks = []
last_id = None


async def _push(record: dict, logger: logging.Logger | None = None):
    async with aiohttp.ClientSession() as session:
        async with session.post(f"{BACKEND_URI}/company", json=record) as resp:
            if resp.status != 200:
                logger.error(f"Error while processing record {resp.status=}")
                logger.error(await resp.text())


async def _loader(
    filepath: str = "./data/gleif.csv",
    limit: int = 10,
    logger: logging.Logger | None = None,
):
    global last_id
    try:
        with open(filepath) as dataset:
            csv_reader = csv.DictReader(dataset, delimiter=",")
            for current_num, record in enumerate(csv_reader, start=1):
                logger.info(f"Processing record no. {current_num}")
                await _push(record)
                last_id = record["LEI"]
                if current_num >= limit:
                    break
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
    return


def run_benchmark(filepath, limit, logger):
    print("Benchmarking the loader")
    if limit == 0:
        print("Benchmarking the loader with no limit")

    if limit != 0:
        print(f"Benchmarking the loader with limit {limit}")

    neo = GraphDatabase.driver("bolt://localhost:7687", auth=("neo4j", "password"))
    report = {}
    logger.setLevel(logging.ERROR)

    with neo.session() as session:
        print("Resetting the database")
        session.run("MATCH (n) DETACH DELETE n")
        print("Database reset done")

        print("Starting the loader")
        start = pendulum.now()
        asyncio.run(_loader(filepath, limit, logger))
        end_api_calls = pendulum.now()
        print("Loader done")

        report["total_time_api_calls"] = (end_api_calls - start).in_words()

        if last_id:
            print(f"Benchmarking the loader with last id {last_id}")
            while True:
                result = session.run(
                    f'MATCH (record:Company {{lei: "{last_id}"}}) RETURN record'
                ).single()
                if result:
                    end_data_write = pendulum.now()
                    data = result.data()["record"]
                    break
            report["total_time_data_write"] = (
                end_data_write - end_api_calls
            ).in_words()
        else:
            print("Can't benchmark with specifying last id")
            return

        report["total_time"] = (end_data_write - start).in_words()

        report.update(
            {
                "total_companies": session.run("MATCH (n) RETURN count(n) as count")
                .single()
                .data()["count"],
                "total_relationships": session.run(
                    "MATCH ()-[r]->() RETURN count(r) as count"
                )
                .single()
                .data()["count"],
                "last_record": data,
            }
        )

        print("Stats:")
        pprint(report, indent=4, depth=2)


@click.command()
@click.option("--filepath", default="./data/gleif.csv", help="Path to the dataset")
@click.option("--limit", default=0, help="Limit the number of records to be processed")
@click.option("--benchmark", default=False, help="Benchmark the loader")
def loader(filepath: str, limit: int, benchmark: bool):
    logger = logging.getLogger(__name__)

    if not benchmark:
        logger.setLevel(logging.DEBUG)
        asyncio.run(_loader(filepath, limit, logger))
        return

    run_benchmark(filepath, limit, logger)


if __name__ == "__main__":
    loader()

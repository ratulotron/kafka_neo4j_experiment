#!/usr/bin/env python

import csv
import logging
from pprint import pprint

import click
import pendulum
from pendulum.period import Period
import requests
from neo4j import GraphDatabase
from smart_open import open

from producer import CompanyProducer


BACKEND_URI = "http://localhost:3000"


tasks: list = []
last_id = None


def _loader(
    logger: logging.Logger,
    filepath: str,
    limit: int = 0,
):
    global last_id

    logger.info(f"Loading data from {filepath}")

    producer = CompanyProducer()
    try:
        with open(filepath) as dataset:
            csv_reader = csv.DictReader(dataset, delimiter=",")
            for current_num, record in enumerate(csv_reader, start=1):
                logger.info(f"Processing record no. {current_num}")
                producer.produce(record)
                last_id = record["LEI"]
                if (current_num >= limit) and (limit != 0):
                    break
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
    producer.close()
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

        _loader(logger, filepath, limit)

        end_api_calls = pendulum.now()
        print("Loader done")
        t: Period = end_api_calls - start
        report["total_time_api_calls"] = t.in_words()

        if last_id:
            print(f"Benchmarking the loader with last id {last_id}")
            while True:
                result = session.run(f'MATCH (record:Company {{lei: "{last_id}"}}) RETURN record').single()
                if result:
                    end_data_write = pendulum.now()
                    data = result.data()["record"]
                    break
            report["total_time_data_write"] = (end_data_write - end_api_calls).in_words()
        else:
            print("Can't benchmark with specifying last id")
            return

        report["total_time"] = (end_data_write - start).in_words()

        # Total companies
        r = session.run("MATCH (n) RETURN count(n) as count").single()
        if r:
            report["total_companies"] = r.data()["count"]

        # Total relationships
        r = session.run("MATCH ()-[r]->() RETURN count(r) as count").single()
        if r:
            report["total_relationships"] = r.data()["count"]

        # Last record
        report["last_record"] = data

        print("Stats:")
        pprint(report, indent=4, depth=2)


@click.command()
@click.option("--filepath", default="./data/gleif.csv", help="Path to the dataset")
@click.option("--limit", default=0, help="Limit the number of records to be processed")
@click.option("--benchmark", default=False, help="Benchmark the loader")
def loader(filepath: str = "/data/gleif.csv", limit: int = 0, benchmark: bool = False):
    logger = logging.getLogger(__name__)

    if not benchmark:
        logger.setLevel(logging.DEBUG)
        _loader(filepath=filepath, limit=limit, logger=logger)
        return

    result = requests.get(f"{BACKEND_URI}/reset")
    if result.status_code != 200:
        logger.error(f"Error while resetting the database {result.status_code=}")
        logger.error(result.text)
        return

    logger.info("Kafka reset done")

    run_benchmark(filepath, limit, logger)


if __name__ == "__main__":
    loader()

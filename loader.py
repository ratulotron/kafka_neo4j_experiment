#!/usr/bin/env python

import csv
from smart_open import open
import click

import aiohttp
import asyncio


BACKEND_URI = 'http://localhost:3000'

tasks = []


async def _push(record: dict):
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{BACKEND_URI}/company', json=record) as resp:
            if resp.status != 200:
                print(f"Error while processing record {resp.status=}")
                print(await resp.text())


async def _loader(filepath: str = "./data/gleif.csv", limit: int = 10):
    try:
        with open(filepath) as dataset:
            csv_reader = csv.DictReader(dataset, delimiter=",")

            for current_num, record in enumerate(csv_reader, start=1):
                print(f"Processing record no. {current_num}")
                await _push(record)
                if current_num >= limit:
                    break
    except Exception as err:
        msg = f"Unexpected {err=}, {type(err)=}"
        print(msg)
    return


@click.command()
@click.option('--filepath', default='./data/gleif.csv', help='Path to the dataset')
@click.option('--limit', default=0, help='Limit the number of records to be processed')
def loader(filepath: str, limit: int):
    asyncio.run(_loader(filepath, limit))


if __name__ == '__main__':
    loader()
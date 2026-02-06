#!/usr/bin/env python3
"""Example code."""

import asyncio
import logging
from os import getenv
from sys import stdout

from aiohttp import ClientSession
from dotenv import load_dotenv

from fiftyfive import Api, Market, NetworkOverview, Overview, Channel

load_dotenv()


async def main():
    """Main module"""

    async with ClientSession() as session:
        api = Api(session, getenv("50FIVE_EMAIL"), getenv("50FIVE_PASSWORD"), Market.BELUX)

        networks = await api.make_requests([NetworkOverview()])
        networks[0] += networks[0]

        details = await api.make_requests(
            [
                Overview(network["IDX"])
                for network in networks[0]
            ]
        )

        result = [c | d[0] for c, d in zip(networks[0], details, strict=True)]
        [print(r) for r in result]


if __name__ == "__main__":
    logging.basicConfig(stream=stdout, level=logging.DEBUG)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())

# Fiftyfive

Python 3 package to retrieve EV charger data from 50five. Uses the hidden
GraphQL API used by the mobile app.

## Installation

```bash
pip3 install fiftyfive
```

## Usage

```Python
import asyncio
import logging
from os import getenv
from sys import stdout

from dotenv import load_dotenv
from httpx import AsyncClient
from sgqlc.operation import Operation

from fiftyfive import Api, schema

load_dotenv()


async def main():
    """Main module"""

    async with AsyncClient() as client:
        api = Api(client, getenv("50FIVE_EMAIL"), getenv("50FIVE_PASSWORD"))
        
        op = Operation(schema.Query)
        cards = op.get_cards()
        cards.items.id()
        cards.items.internal_id()
        cards.items.external_id()
        cards.items.expiry_date()

        data = await api.make_request(op)

        if data.get("errors"):
            raise RuntimeError("Get cards failed")

        print((op + data).get_cards)


if __name__ == "__main__":
    logging.basicConfig(stream=stdout, level=logging.DEBUG)
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
```

# Fiftyfive

Python 3 package to retrieve EV charger data from 50five

## Installation

```bash
pip3 install fiftyfive
```

## Usage

```Python
import asyncio

from aiohttp import ClientSession
from fiftyfive import Api, CustomerType, Market, NetworkOverview


async def main():
    """Main module"""

    async with ClientSession() as session:
        api = Api(session, "email", "password", Market.BELUX, CustomerType.FORMER_SHELL)

        result = await api.make_requests([NetworkOverview()])
        print(result)


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main())
```

## WARNING

50five uses separate endpoints depending on the market (belux, nl, de, ...) as
well as whether or not you were migrated over from Shell Recharge. As I myself
only have access to an account in the belux market as an ex-Shell customer, I
cannot do any testing/reverse engineering on the other markets, so I can't give
any guarantee anything will work for accounts in them.

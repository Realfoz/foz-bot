# will be the main file running any logic and general main flow stuff

from bot import *
import asyncio


def main():
    asyncio.run(run_bot())


if __name__ == "__main__":
    main()

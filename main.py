# will be the main file running any logic and general main flow stuff

from bot import run_bot
import asyncio


def main():
    asyncio.run(run_bot())


if __name__ == "__main__":
    main()

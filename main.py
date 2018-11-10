#!/usr/bin/env python3
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

NAME = "Rigel"


def say(message):
    print(message)


async def main():
    while True:
        line = await loop.run_in_executor(None, input, "? ")
        cmd, *args = line.split(" ")
        if cmd:
            if cmd.lower() == "say":
                message = " ".join(args)
                say(message)
            else:
                logging.error("Unknown command: %s", cmd)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = (main(), )
    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except KeyboardInterrupt:
        pass

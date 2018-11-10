#!/usr/bin/env python3
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

NAME = "Rigel"


def say(message):
    print(message)


async def bot():
    reader, writer = await asyncio.open_connection(
        "irc.freenode.net",
        6667,
        ssl=False
    )
    writer.write(b"NICK rigel-pycon18\r\n")
    writer.write(b"USER Rigel * * *\r\n")
    while not reader.at_eof():
        line = await reader.readline()
        line = line.decode('utf-8')
        if line:
            print(line)
            if "001" in line:
                writer.write(b"JOIN #pycoin18\r\n")
                writer.write(b"NAMES #pycoin18\r\n")


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
    tasks = (main(), bot())
    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except KeyboardInterrupt:
        pass

#!/usr/bin/env python3
import asyncio


def say(msg):
    print(msg)


def _main():
    while True:
        msg = input("? ")
        try:
            cmd, arg = msg.split(" ")
        except ValueError:
            pass
        else:
            if cmd == "say":
                say(arg)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = (_main(), )
    try:
        loop.run_until_complete(asyncio.gather(*tasks))
    except KeyboardInterrupt:
        pass


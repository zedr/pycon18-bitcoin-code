#!/usr/bin/env python3

def say(msg):
    print(msg)

if __name__ == "__main__":
    while True:
        msg = input("? ")
        try:
            cmd, arg = msg.split(" ")
        except ValueError:
            pass
        else:
            if cmd == "say":
                say(arg)

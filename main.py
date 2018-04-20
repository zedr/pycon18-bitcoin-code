#!/usr/bin/env python3

def main():
    while True:
        cmd, *args = input("? ").split(" ")
        if cmd.lower() == "echo":
            print(" ".join(args))
        else:
            print("Comando sconosciuto: {}".format(cmd))

if __name__ == "__main__":
    main()
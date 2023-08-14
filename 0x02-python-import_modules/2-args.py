#!/usr/bin/python3
from sys import argv


def main():
    if len(argv) == 1:
        print("{:d} arguments{}".format(len(argv) - 1, '.'))
        return
    elif len(argv) == 2:
        print("{} argument{}:".format(len(argv) - 1, ""))
    else:
        print("{} argument{}:".format(len(argv) - 1, "s"))

    if (len(argv) >= 2):
        for counter, argument in enumerate(argv[1:], start=1):
            print("{}: {}".format(counter, argument))


if __name__ == "__main__":
    main()

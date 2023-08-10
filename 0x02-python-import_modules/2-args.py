#!/usr/bin/python3
import sys


def main():
    args = sys.argv[1:]
    arg_num = len(args)
    if(arg_num == 0):
        print("0 arguments.")
        return

    if(arg_num >= 1):
        print("{} argument{}:".format(arg_num, "" if arg_num == 1 else 's'))

    for count, arg in enumerate(args, start=1):
        print("{}: {}".format(count, arg))


if __name__ == "__main__":
    main()

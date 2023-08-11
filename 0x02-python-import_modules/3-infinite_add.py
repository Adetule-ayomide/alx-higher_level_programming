#!/usr/bin/python3
from sys import argv


def main():
    args = len(argv) - 1
    total = 0
    if(args == 0):
        print("{:d}".format(args))
    elif(args == 1):
        print("{:d}".format(int(argv[1])))
    else:
        for i in argv[1:]:
            total += int(i)
        print("{:d}".format(total))


if __name__ == "__main__":
    main()

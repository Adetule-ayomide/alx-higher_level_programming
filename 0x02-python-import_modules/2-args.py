#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    args = argv[1:]
    arg_num = len(args)
    if(arg_num == 0):
        print("{:d} arguments.".format(0))
    elif(arg_num >= 1):
        print("{:d} argument{}:".format(arg_num, "" if arg_num == 1 else 's'))

    for count, arg in enumerate(args, start=1):
        print("{:d}: {}".format(count, arg))

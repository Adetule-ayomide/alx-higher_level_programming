#!/usr/bin/python3


"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """a function that reads file"""
    with open("UTF8", "r") as filename:
        file = filename.readlines()

    for i in file:
        print(file)

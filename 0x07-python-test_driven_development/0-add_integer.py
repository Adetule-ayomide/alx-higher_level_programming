#!/usr/bin/python3

"""module containing add function for unit test"""


def add_integer(a, b=98):
    """add_integer - function to add two integer
        argument:
        @a: first integer
        @b: second integer which as a default value of 98
    """

    if type(a) is not int or type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int or type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

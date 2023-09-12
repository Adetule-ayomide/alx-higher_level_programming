#!/usr/bin/python3


"""a function that returns the list of available
    attributes and methods of an object:

    Prototype: def lookup(obj):
    Returns a list object
"""


def lookup(obj):
    """function that lookup and return a list"""
    attributes_and_methods = dir(obj)
    return attributes_and_methods

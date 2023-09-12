#!/usr/bin/python3


"""a function that returns True if the object is exactly an
    instance of the specified class ; otherwise False.

    Prototype: def is_same_class(obj, a_class):
    You are not allowed to import any module
"""


def is_same_class(obj, a_class):
    """A function that return true or false if an object
        exactly an instance

        Args:
            @obj: object to check
            @a_class: instance of the specified class
    """
    if (type(obj) == a_class):
        return True
    else:
        return False

#!/usr/bin/python3

"""a function that adds a new attribute to an object if it’s possible"""


def add_attribute(obj, attribute_name, attribute_value):
    """function that add attribute"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attribute_name, attribute_value)
    else:
        raise TypeError("can't add new attribute")

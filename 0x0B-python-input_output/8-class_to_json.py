#!/usr/bin/python3

"""a function that returns the dictionary description with simple
    data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object
"""

import json


def class_to_json(obj):
    """Args:
        obj: The object
    """
    serializable_data = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_data[key] = value
    return serializable_data

#!/usr/bin/python3

"""a function that returns the JSON representation of an object (string)"""

import json


def to_json_string(my_obj):
    """Args:
        A function that returnjson representation
    Return:
        json representation of an object (string)
    """
    return json.dumps(my_obj)

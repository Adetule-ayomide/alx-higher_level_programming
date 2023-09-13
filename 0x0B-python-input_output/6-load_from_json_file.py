#!/usr/bin/python3

""" a function that creates an Object from a JSON file"""

import json


def load_from_json_file(filename):
    """
        Args:
            filename: the name of the file
            create an object from a json file
    """
    with open(filename, "r", encoding="utf-8") as file:
        obj = json.load(file)
        return obj

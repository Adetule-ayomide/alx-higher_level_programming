#!/usr/bin/python3

"""a function that writes an Object to a text file,
    using a JSON representation
"""

import json


def save_to_json_file(my_obj, filename):
    """Args:
        my_obj: the object
        filename: the name of the file
    """
    with open(filename, "w", encoding='utf-8') as file:
        json_str = json.dumps(my_obj, ensure_ascii=False)
        file.write(json_str)

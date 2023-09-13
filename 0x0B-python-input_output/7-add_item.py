#!/usr/bin/python3

"""a script that adds all arguments to a Python list,
    and then save them to a file
"""

import sys
import os


if os.path.exists("add_item.json"):
    items = load_from_json_file("add_item.json")
else:
     items = []

items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")

#!/usr/bin/python3


""" a function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
"""


def write_file(filename="", text=""):
    """
    Args:
        filename: name of the file to append to
        text: text to be written
    Returns:
    number of characters added
    """
    with open(filename, "a", encoding='utf-8') as file:
        file.write(text)
        num_written = len(text)
        return num_written

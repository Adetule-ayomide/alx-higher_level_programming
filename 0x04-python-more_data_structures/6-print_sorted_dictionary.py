#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    new_dict = sorted(a_dictionary)
    for key in new_dict:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
    return

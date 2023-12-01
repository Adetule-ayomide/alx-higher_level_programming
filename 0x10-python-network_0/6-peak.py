#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """A function that finds a peak"""
    if list_of_integers is None or list_of_integers == []:
        return None

    max_number = max(list_of_integers)
    max_index = list_of_integers.index(max_number)

    if len(list_of_integers) == 1:
        return max_number

    if len(list_of_integers) >= 2:
        if max_index == 0 or max_index == len(list_of_integers) - 1:
            return max_number

    if len(list_of_integers) >= 3:
        if list_of_integers[max_index - 1] <= list_of_integers[max_index]\
                >= list_of_integers[max_index + 1]:
            return max_number

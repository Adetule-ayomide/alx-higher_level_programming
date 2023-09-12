#!/usr/bin/python3


"""a class MyList that inherits from list:

    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    You can assume that all the elements of the list will be of type int
"""


class MyList(list):
    """a class MyList that inherits from list"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
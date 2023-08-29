#!/usr/bin/python3

"""a class that defines a square"""


class Square:
    """define a class square"""

    
    def __init__(self, size=0):
        """declare a private instance
        attribute

        Args:
            size (int): the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

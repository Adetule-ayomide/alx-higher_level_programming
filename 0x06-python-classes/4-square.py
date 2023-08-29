#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Initialize a the Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        "To retrieve the size"

        return self.__size

    def area(self):
        """The area calculation"""

        return self.__size ** 2

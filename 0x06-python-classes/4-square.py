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

    @property
    def size(self):
        """To retrieve the size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """The area calculation"""
        return self.__size ** 2

#!/usr/bin/python3

"""a class Square that defines a square"""


class Square:
    """define a class square"""

    
    def __init__(self, size=0):
        """declare a private instance attribute

        Args:
            size (int): the size of the square
        """

        self.__size = int(size)

    
    def area(self):
        """This is a method that calc the area"""

        return self.__size ** 2


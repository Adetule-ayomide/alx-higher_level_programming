#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """A class rectangle

    args:
        @width: width of rectangle
        @height: height of rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter function: returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter function : set values"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function: returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter function : set values"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

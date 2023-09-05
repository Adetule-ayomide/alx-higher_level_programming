#!/usr/bin/python3
"""A class Rectangle that defines a rectangle"""


class Rectangle:
    """  a class Rectangle that defines a rectangle by:
        (based on 0-rectangle.py)
        @width: width of the rectangle
        @height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter function: a function that returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ setter function: a function that set the value"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter function: a function that returns height"""
        return self.__height

    @height.setter
    def height(self, value):
        """ setter function: a function that set the value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

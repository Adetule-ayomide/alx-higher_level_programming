#!/usr/bin/python3


"""a class BaseGeometry (based on 5-base_geometry.py).
    Public instance method: def area(self): that raises an
    Exception with the message area() is not implemented
    You are not allowed to import any module
"""


class BaseGeometry:
    """A basegeometry class"""
    def area(self):
        """A function that raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.value = value

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

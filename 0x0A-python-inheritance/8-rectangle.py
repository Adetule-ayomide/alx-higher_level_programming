#!/urs/bin/python3

"""a class Rectangle that inherits from BaseGeometry (7-base_geometry.py)."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle class that inherit from basegeometry"""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.validator("height", height)
        self.__heigth = height

#!/usr/bin/python3
"""
Creating class will import from base geometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class inheriting from BaseGemetry
    """
    def __init__(self, width, height):
        """
        init the value
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        return the area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        return the a string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

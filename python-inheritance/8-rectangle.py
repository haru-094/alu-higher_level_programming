#!/usr/bin/python3
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
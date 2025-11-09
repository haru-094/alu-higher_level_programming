#!/usr/bin/python3
"""
inherting class form rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class inherting
    """
    def __init__(self, size):
        """
        init the attr
        """
        self.integer_validator('size', size)
        self.__size = size
        super.__init__(size, size)

    def area(self):
        """
        return the area
        """
        return self.__size * self.__size

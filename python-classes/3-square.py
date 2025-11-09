#!/usr/bin/python3
"""
Create class square with size
"""


class Square:
    """
    square class
    """

    def __init__(self, size=0):
        """
        init the size and square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        do the math and return area
        """
        return self.__size ** 2

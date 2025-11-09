#!/usr/bin/python3
"""
Cretae class square with size attribute
using setter/getter
"""


class Square:
    """
    Square class

    Attributes:
        __size(int): size of square
    """

    def __init__(self, size=0):
        """
        init new square

        Args:
            size(int, optional): size of square default is 0
        """
        self.size = size

    @property
    def size(self):
        """
        return the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size of square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        do the math and return the area
        """
        return self.__size ** 2

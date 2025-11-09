#!/usr/bin/python3
"""
Create class square with private size attr
"""


class Square:
    """
    Square class
    """

    def __init__(self, size=0):
        """
        init the size attr
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
        set size value
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

    def my_print(self):
        """
        return the result of square
        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            print("#" * self.__size)

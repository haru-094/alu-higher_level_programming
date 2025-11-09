#!/usr/bin/python3
"""
Create class square with size
"""


class Square:
    """
    class square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        init the size and position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        return size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        set the size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        return the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        set the position value
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        do the math and return area
        """
        return self.__size ** 2

    def my_print(self):
        """
        return the result for square
        """
        if self.__size == 0:
            print()
            return

        print("\n" * self.__position[1], end="")

        hr_offest = " " * self.__position[0]
        for _ in range(self.__size):
            print(hr_offest + '#' * self.__size)

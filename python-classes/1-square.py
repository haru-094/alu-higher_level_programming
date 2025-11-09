#!/usr/bin/python3
"""
Create class square with private attribute
"""


class Square:
    """
    Class square
    contain attribute size to count
    """
    def __init__(self, size):
        """
        init suqare instance

        Args:
            size(int): the size of new square
        """
        self.__size = size

#!/usr/bin/python3
"""
Create class square with size vaildation
"""


class Square:
    """
    square with vaildation for size
    """

    def __init__(self,size=0):
        """
        init the instance

        Args:
            size(int, optional): create new square size
        
        Rasie:
            TypeError: if size not integer
            valueError: if the size is less 0
        """
        if not isinstance(size, int):
            raise TypeError("size is not integer")
        if size < 0:
            raise ValueError("size must be greater than 0")
        self.__size = size

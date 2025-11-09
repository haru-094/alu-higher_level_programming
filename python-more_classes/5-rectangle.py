#!/usr/bin/python3
"""
Create class rectangle
"""


class Rectangle:
    """
    rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        class init
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set the width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        do the math and get area
        """
        return self.width * self.height

    def perimeter(self):
        """
        do the math and get perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        returnt the string of rectangle
        """
        if self.width == 0 or self.height == 0:
            return ""

        rows = ["#" * self.width for _ in range(self.height)]
        return "\n".join(rows)

    def __repr__(self):
        """
        return a string of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        print msg for delete
        """
        print("Bye rectangle...")

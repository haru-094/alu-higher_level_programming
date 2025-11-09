#!/usr/bin/python3
"""
Create class Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    # Compatibility alias for printsymbol (no underscore) used in tests
    @property
    def printsymbol(self):
        return self.print_symbol

    @printsymbol.setter
    def printsymbol(self, value):
        self.print_symbol = value

    def area(self):
        """Area"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Visual rectangle with print_symbol"""
        if self.width == 0 or self.height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Formal string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Destructor"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

#!/usr/bin/python3
"""
This module provides the Square class.

The Square class inherits from Rectangle and represents a square
with size and position (x, y) attributes.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    A Square is a special Rectangle with equal width and height.

    Attributes:
        size (int): The size of the square (width and height)
        x (int): The x coordinate of the square
        y (int): The y coordinate of the square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square (width and height)
            x (int, optional): The x coordinate. Defaults to 0.
            y (int, optional): The y coordinate. Defaults to 0.
            id (int, optional): The id for the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Return string representation of the Square.

        Returns:
            str: [Square] (<id>) <x>/<y> - <size>
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """
        Update the Square attributes with no-keyword or key-worded arguments.

        Args:
            *args: Variable length argument list (no-keyword arguments)
                1st argument: id attribute
                2nd argument: size attribute
                3rd argument: x attribute
                4th argument: y attribute
            **kwargs: Key-worded arguments (dictionary)
                Each key represents an attribute to update
                Only used if *args is empty
        """
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.

        Returns:
            dict: Dictionary containing id, size, x, and y
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

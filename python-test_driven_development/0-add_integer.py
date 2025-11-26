#!/usr/bin/python3
"""
This module provides a function for adding two integers.

The module contains the add_integer function which adds two numbers
after converting them to integers if they are floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98

    Returns:
        int: The sum of a and b as an integer

    Raises:
        TypeError: If a or b is not an integer or float

    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

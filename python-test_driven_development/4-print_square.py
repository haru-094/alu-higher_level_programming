#!/usr/bin/python3
"""
This module provides a function for printing squares.

The module contains the print_square function which prints a square
using the '#' character.
"""


def print_square(size):
    """
    Prints a square with the character # of the given size.

    Args:
        size: The size length of the square (must be a non-negative integer)

    Returns:
        None

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0

    Examples:
        >>> print_square(3)
        ###
        ###
        ###
        >>> print_square(1)
        #
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

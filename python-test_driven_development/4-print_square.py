#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character # of the given size.

    size must be an integer, otherwise raises TypeError:
    "size must be an integer"

    If size is less than 0, raises ValueError:
    "size must be >= 0"

    If size is a float, raises TypeError:
    "size must be an integer"
    """
    if isinstance(size, float):
        raise TypeError("size must be an integer")

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    a and b must be integers or floats, otherwise raises TypeError.
    Floats are casted to integers before addition.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

#!/usr/bin/python3
"""
This module provides a function to find the max integer in a list.

The module contains the max_integer function which finds and returns
the maximum integer in a list of integers.
"""


def max_integer(list=[]):
    """
    Finds and returns the max integer in a list of integers.

    Args:
        list: A list of integers (defaults to empty list)

    Returns:
        int: The maximum integer in the list, or None if list is empty

    Examples:
        >>> max_integer([1, 2, 3, 4])
        4
        >>> max_integer([1, 3, 4, 2])
        4
        >>> max_integer([])

    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

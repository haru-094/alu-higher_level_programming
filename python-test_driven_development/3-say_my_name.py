#!/usr/bin/python3
"""
This module provides a function for printing names.

The module contains the say_my_name function which prints a formatted
string with a person's first and last name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string), defaults to ""

    Returns:
        None

    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string

    Examples:
        >>> say_my_name("John", "Smith")
        My name is John Smith
        >>> say_my_name("Bob")
        My name is Bob 
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

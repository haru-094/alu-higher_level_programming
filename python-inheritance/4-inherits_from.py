#!/usr/bin/python3
"""
function to check of object
"""


def inherits_from(obj, a_class):
    """
    return true of object is instance
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

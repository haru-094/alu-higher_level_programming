#!/usr/bin/python3
"""
Create function of class json
"""


def class_to_json(obj):
    """
    return the dict with description
    """
    return obj.__dict__

#!/usr/bin/python3
"""
Create function to append string
"""


def append_write(filename="", text=""):
    """
    appending to file
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

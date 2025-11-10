#!/usr/bin/python3
"""
create function that write in the file
"""


def write_file(filename="", text=""):
    """
    write a string into the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)

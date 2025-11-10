#!/usr/bin/python3
"""
Create function that read file text
"""


def read_file(filename=""):
    """
    read the file and print the content
    """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')

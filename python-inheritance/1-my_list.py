#!/usr/bin/python3
"""
Creating class
"""


class MyList(list):
    """
    creating class mylist
    """
    def print_sorted(self):
        """
        sort the result then printed
        """
        print(sorted(self))

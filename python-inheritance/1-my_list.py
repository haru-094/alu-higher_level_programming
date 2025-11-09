#!/usr/bin/python3
class Mylist(list):
    """
    list class
    """
    def print_sorted(self):
        """
        sort the result then printed
        """
        print(sorted(self))

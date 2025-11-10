#!/usr/bin/python3
"""
Create class student
"""


class Student:
    """
    class student
    """
    def __init__(self, first_name, last_name, age):
        """
        init the attr
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """
            return dict
            """
            return self.__dict__

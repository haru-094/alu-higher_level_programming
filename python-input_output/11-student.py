#!/usr/bin/python3
"""
Create class student
"""


class Student:
    """
    student class
    """
    def __init__(self, first_name, last_name, age):
        """
        init attr
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return dict
        """
        if isinstance(attrs, list) and all(
                isinstance(item, str) for item in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """
        reload all attr
        """
        for key, value in json.items():
            setattr(self, key, value)

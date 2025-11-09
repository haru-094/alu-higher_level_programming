#!/usr/bin/python3
"""
base gemoetry class
"""


class BaseGeometry:
    """
    BaseGemotery class
    """
    def area(self):
        """
        raise error with msg
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validate if the value is positve
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

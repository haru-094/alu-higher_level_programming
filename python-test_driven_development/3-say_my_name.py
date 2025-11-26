#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    first_name and last_name must be strings,
    otherwise raises TypeError with the messages:
    "first_name must be a string" or "last_name must be a string"
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")

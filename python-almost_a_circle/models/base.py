#!/usr/bin/python3
"""
This module provides the Base class for all other classes in the project.

The Base class manages the id attribute and serves as the foundation
for all future classes in this project.
"""
import json


class Base:
    """
    Base class for managing id attribute across all instances.

    Attributes:
        __nb_objects (int): Private class attribute tracking number of objects

    Args:
        id (int, optional): The id for the instance. If None, auto-increments.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize a Base instance.

        Args:
            id (int, optional): The id for the instance. If None, 
                                __nb_objects is incremented and assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries

        Returns:
            str: JSON string representation of list_dictionaries,
                 or "[]" if None or empty
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Return the list represented by the JSON string json_string.

        Args:
            json_string (str): A string representing a list of dictionaries

        Returns:
            list: The list represented by json_string,
                  or an empty list if json_string is None or empty
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list_objs to a file.

        Args:
            cls: The class (Rectangle or Square)
            list_objs (list): A list of instances that inherit from Base

        The filename is <Class name>.json (e.g., Rectangle.json).
        If list_objs is None, saves an empty list.
        """
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)

        with open(filename, "w") as f:
            f.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return an instance with all attributes already set.

        Args:
            cls: The class (Rectangle or Square)
            **dictionary: A dictionary of attributes to set

        Returns:
            An instance of cls with attributes set from dictionary
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Return a list of instances loaded from a JSON file.

        Args:
            cls: The class (Rectangle or Square)

        Returns:
            list: A list of instances of cls. Returns an empty list
                  if the file doesn't exist.

        The filename is <Class name>.json (e.g., Rectangle.json).
        """
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

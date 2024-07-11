#!/usr/bin/python3
""" Base class """
import json


class Base:
    """
    The Base class serves as the base class for other classes in the project.
    It provides a unique identifier for each instance created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new instance of the Base class.

        Args:
            id (int): The unique identifier for the instance. If not provided,
            a new identifier will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """
        Convert a list of dictionaries to a JSON string representation.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: A JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

#!/usr/bin/python3
""" this module contain student class """


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the student.

        Args:
            attrs (list):
                Optional list of attributes to
                include in the dictionary.
                If provided, only the specified
                attributes will be included.
                If not provided, all attributes will be included.

        Returns:
            dict: A dictionary containing the student's attributes.

        """
        if type(attrs) is list and \
                all(type(lol) is str for lol in attrs):
            lols = {}
            for lol in attrs:
                if hasattr(self, lol):
                    lols[lol] = getattr(self, lol)
            return lols
        return self.__dict__

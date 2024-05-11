#!/usr/bin/python3
""" this module contain class_to_json function"""


def class_to_json(obj):
    """
    Converts a Python object to a dictionary representation.

    Args:
        obj: The object to convert.

    Returns:
        A dictionary representation of the object.
    """
    return obj.__dict__

#!/usr/bin/python3
""" this module contain from_json_string function """
import json


def from_json_string(my_str):
    """
    Converts a JSON string representation into a Python object.

    Args:
        my_str (str): The JSON string to be converted.

    Returns:
        object: The Python object representation of the JSON string.

    """
    return json.loads(my_str)

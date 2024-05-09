#!/usr/bin/python3
""" this module contain 5-save_to_json_file function """
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
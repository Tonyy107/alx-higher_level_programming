#!/usr/bin/python3
""" this module contain add_item function """
import sys
import os

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file


if os.path.exists("add_item.json"):
    b = load_from_json_file("add_item.json")
else:
    b = []

a = sys.argv[1:]
b.extend(a)

save_to_json_file(b, "add_item.json")

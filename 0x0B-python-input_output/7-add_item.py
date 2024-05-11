#!/usr/bin/python3
""" this module contain add_item function """
import sys

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
try:
    load_from_json_file("add_item.json")
except FileNotFoundError:
    argss = []

argss.extend(sys.argv[1:])

save_to_json_file(argss, "add_item.json")
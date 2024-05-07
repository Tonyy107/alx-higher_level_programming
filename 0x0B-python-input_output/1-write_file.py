#!/usr/bin/python3
""" this module have write_file function """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(text)
    return len(text)
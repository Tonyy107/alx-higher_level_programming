#!/usr/bin/python3
""" this module contain append_write function """


def append_write(filename="", text=""):
    """
    Appends the given text to the end of the specified file.

    Args:
        filename (str): The name of the file to append the text to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'a', encoding="UTF8") as file:
        return file.write(text)

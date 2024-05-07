#!/usr/bin/python3
""" this module have write_file function """


def write_file(filename="", text=""):
    """
    Writes the given text to a file.

    Args:
        filename (str): The name of the file to write to.
        text (str): The text to write to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w') as file:
        file.write(text)
    return len(text)

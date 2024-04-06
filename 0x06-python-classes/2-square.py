#!/usr/bin/python3
"""this is Square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size: The size of the new square.
        """
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

#!/usr/bin/python3
"""square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            size: it's size of square dude!!!
            x: the same x as before
            y: the same y as before
            id: the same id as before
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        str - it return string
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id,
            self.x,
            self.y,
            self.height
            )

    @property
    def size(self):
        """size getter"""
        return self.height

    @size.setter
    def size(self, size):
        """size setter"""
        self.height = size
        self.width = size
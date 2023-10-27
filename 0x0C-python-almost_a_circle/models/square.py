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

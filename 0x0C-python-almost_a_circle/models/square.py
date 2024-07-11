#!/usr/bin/python3
""" Square module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square shape.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square object.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square's position
            (default is 0).
            y (int): The y-coordinate of the square's position
            (default is 0).
            id (int): The unique identifier of the square
            (default is None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Returns a string representation of the Square object.

        The string includes the object's ID, coordinates (x, y),
        and height.

        Returns:
            str: A string representation of the Square object.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

    @property
    def size(self):
        """Returns the size of the square."""
        return self.height

    @size.setter
    def size(self, size):
        """Set the size of the square.

            Args:
                size (int): The size of the square.

        """
        self.width = size
        self.height = size

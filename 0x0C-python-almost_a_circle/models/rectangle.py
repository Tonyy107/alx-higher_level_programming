#!/usr/bin/python3
""" rectangle class """
from models.base import Base


class Rectangle(Base):
    """
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the rectangle's position.
        y (int): The y-coordinate of the rectangle's position.
        id (int): The unique identifier of the rectangle.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new instance of the Rectangle class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the rectangle's position.
                Defaults to 0.
            y (int, optional): The y-coordinate of the rectangle's position.
                Defaults to 0.
            id (int, optional): The unique identifier of the rectangle.
                Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def checker(self, name_atr, atr, hewi=True):
        """
        Check the validity of an attribute value.

        Args:
            name_atr (str): The name of the attribute being checked.
            atr (int): The value of the attribute being checked.
            hewi (bool, optional): Flag indicating whether the attribute
            must be greater than zero. Defaults to True.

        Raises:
            TypeError: If the attribute is not an integer.
            ValueError: If the attribute is not valid based on
            the specified conditions.

        Returns:
            None
        """
        if not isinstance(atr, int):
            raise TypeError(f"{name_atr} must be an integer")
        else:
            if hewi:
                if atr <= 0:
                    raise ValueError(f"{name_atr} must be > 0")
            if not hewi:
                if atr < 0:
                    raise ValueError(f"{name_atr} must be >= 0")

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            The area of the rectangle.
        """
        return self.width * self.height

    def display(self):
        """
        Display the rectangle by printing '#' characters in the shape of the rectangle.
        """
        for i in range(self.height):
            for e in range(self.width):
                print("#", end="")
            print()

    @property
    def width(self):
        """
        Gets the width of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Sets the width of the rectangle.

        Args:
            width (int): The new width of the rectangle.
        """
        self.checker("width", width, True)
        self.__width = width

    @property
    def height(self):
        """
        Gets the height of the rectangle.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Sets the height of the rectangle.

        Args:
            height (int): The new height of the rectangle.
        """
        self.checker("height", height, True)
        self.__height = height

    @property
    def x(self):
        """
        Gets the x-coordinate of the rectangle's position.

        Returns:
            int: The x-coordinate of the rectangle's position.
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        Sets the x-coordinate of the rectangle's position.

        Args:
            x (int): The new x-coordinate of the rectangle's position.

        Returns:
            None
        """
        self.checker("x", x, False)
        self.__x = x

    @property
    def y(self):
        """
        Gets the y-coordinate of the rectangle's position.

        Returns:
            int: The y-coordinate of the rectangle's position.
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Sets the y-coordinate of the rectangle's position.

        Args:
            y (int): The new y-coordinate of the rectangle's position.
        """
        self.checker("y", y, False)
        self.__y = y

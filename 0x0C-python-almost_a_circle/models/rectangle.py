#!/usr/bin/python3
"""rectangle module"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        init - initialization
        Args:
            width: it just a width
            height: it just a height
            x: it equal to 0
            y: it equal to 0 too
            id: object id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        str - it return string
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id,
            self.x,
            self.y,
            self.width,
            self.height
            )

    def checker(self, input, name_of_att, wihe=True):
        """
        checker - method to check inputs
        Args:
            input: the variable that goona be checked
            name_of_att: name of the variable
            wihe: width or height
        """
        if not isinstance(input, int):
            raise TypeError("{} must be an integer".format(name_of_att))
        if wihe:
            if input <= 0:
                raise ValueError("{} must be > 0".format(name_of_att))
        elif input < 0:
            raise ValueError("{} must be >= 0".format(name_of_att))

    @property
    def width(self):
        """ width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ width setter """
        self.checker(width, "width",)
        self.__width = width

    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ height setter """
        self.checker(height, "height")
        self.__height = height

    @property
    def x(self):
        """ x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ x setter """
        self.checker(x, "x", False)
        self.__x = x

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ y setter """
        self.checker(y, "y", False)
        self.__y = y

    def area(self):
        """
        area: area of rectangle
        """
        return self.width * self.height

    def display(self):
        """
        display: method to display the shape of rectangle
        """
        for y in range(self.y):
            print()
        for i in range(self.height):
            for x in range(self.x):
                print(' ', end='')
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        update - to update variables
        """
        lst = (self.id, self.width, self.height, self.x, self.y)
        if args:
            self.id, self.width, self.height, self.x, self.y = \
                args + lst[len(args):len(lst)]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

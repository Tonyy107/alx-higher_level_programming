#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """

    def __init__(self, size=0, position=(0, 0)):
        """ init """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):

        a = isinstance(value, int)
        if a:
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ area method """
        return (self.__size*self.__size)

    def my_print(self):
        """ print method """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for a in range(self.__size):
            print("".join(" " for k in range(self.__position[0])), end="")
            print("".join("#" for z in range(self.__size)))

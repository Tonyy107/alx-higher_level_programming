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
        a = isinstance(value[0], int)
        b = isinstance(value[1], int)
        c = isinstance(value, tuple)
        if a and b and c and value[0] >= 0 and value[1] >= 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

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
            pass

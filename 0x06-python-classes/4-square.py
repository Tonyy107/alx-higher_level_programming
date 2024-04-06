#!/usr/bin/python3
""" defines a class named Square """


class Square:
    """ defines a function named __init__ """
    def __init__(self, size=0):
        """ init """
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):

        if value.isdigit():
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ area method """
        return (self.__size*self.__size)

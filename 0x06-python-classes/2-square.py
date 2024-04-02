#!/usr/bin/python3
"square class"


class Square:
    "square class"
    def __init__(self, size=0):
        if size != int:
            TypeError("size must be an integer")
        if size < 0:
            ValueError("size must be >= 0")
        else:
            self.__size = size

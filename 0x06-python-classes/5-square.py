#!/usr/bin/python3
"this is square class"


class Square:
    "square class"
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self._Square__size = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size > 0:
            for i in range(self._Square__size):
                for f in range(self._Square__size):
                    print('#',end="")
                print("")
        else:
            print("")
        
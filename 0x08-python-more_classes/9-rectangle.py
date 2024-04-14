#!/usr/bin/python3
""" rectangle module """


class Rectangle:
    """ rectangle class """
    number_of_instances = 0
    print_symbol = "#"
    exception_occured = False

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter """
        if isinstance(value, int) is not True:
            self.exception_occured = True
            raise TypeError("width must be an integer")
        if value < 0:
            self.exception_occured = True
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter """
        if isinstance(value, int) is not True:
            self.exception_occured = True
            raise TypeError("height must be an integer")
        if value < 0:
            self.exception_occured = True
            raise ValueError("height must be >= 0")
        self.__height = value

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance that is a square w/ h==w==size"""
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def area(self):
        return self.__height*self.__width

    def perimeter(self):
        if self.__height <= 0 or self.__width <= 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for a in range(self.__height):
            for e in range(self.__width):
                rect.append(str(self.print_symbol))
            if a != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        rect = "Rectangle(" + str(self.__width) + \
            ", " + str(self.__height) + ")"
        return rect

    def __del__(self):
        type(self).number_of_instances -= 1
        if self.exception_occured is False:
            print("Bye rectangle...")

#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle


my_rectangle = Rectangle(2, "3")
print(my_rectangle.__dict__)

my_rectangle1 = Rectangle("2", 3)
print(my_rectangle1.__dict__)
#!/usr/bin/python3
"this is square class"


class Square:
    "square class"
    def __init__(self, size=0):
        self. _Square__size = size
        if size =={}:
            print('size must be an integer')
        elif size < 0 :
            print('size must be >= 0')
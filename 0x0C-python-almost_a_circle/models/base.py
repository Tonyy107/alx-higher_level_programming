#!/usr/bin/python3
"""
this is base class
"""

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """
        this is init method
        """
        if id is not None:
            self.id = id
        else:
             Base.__nb_objects += 1
             self.id = Base.__nb_objects 

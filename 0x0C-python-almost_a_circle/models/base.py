#!/usr/bin/python3

#base calss

class base:
    __nb_objects = 0

    def __init__(self, id=None):
        #this is init method
        if id is not None:
            self.id = id
        else:
             base.__nb_objects += 1
             self.id = base.__nb_objects 

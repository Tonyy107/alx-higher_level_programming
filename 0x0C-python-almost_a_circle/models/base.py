#!/usr/bin/python3
#base calss

class base:
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is not None:
            self.id = id

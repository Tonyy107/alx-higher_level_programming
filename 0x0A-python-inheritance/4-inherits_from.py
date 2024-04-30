#!/usr/bin/python3
""" 4-inherits_from module """


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that
    inherited(directly or indirectly) from the specified
    class; otherwise False.
    """
    return isinstance(obj, a_class) and \
        not obj.__class__ is a_class

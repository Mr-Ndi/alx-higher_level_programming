#!/usr/bin/python3
"""returning True if the object is exactly
    an instance of the specified False otherwise
"""


def is_same_class(obj, a_class):
    """This function that returns True if the object
        is exactly an instance of the specified class
        otherwise return False
    """
    return type(obj) == a_class

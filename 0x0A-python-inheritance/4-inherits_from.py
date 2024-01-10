#!/usr/bin/python3
"""returning True if the object is
    an instance of the specified False otherwise
"""


def inherits_from(obj, a_class):
    """This function that returns True if the object
        is exactly an instance of the specified class
        otherwise return False
    """
    return isinstance(obj, a_class)

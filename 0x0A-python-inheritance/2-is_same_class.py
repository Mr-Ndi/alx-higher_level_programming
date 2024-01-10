#!/usr/bin/python3
"""returning True if the object is exactly
    an instance of the specified False otherwise
"""


def is_same_class(obj, a_class):
    if type(obj) != a_class:
        return False
    return True

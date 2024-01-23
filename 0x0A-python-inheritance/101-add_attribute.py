#!/usr/bin/python3

'''a function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, akk, value):
     """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        akk (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, akk, value)

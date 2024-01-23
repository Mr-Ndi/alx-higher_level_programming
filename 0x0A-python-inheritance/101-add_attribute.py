#!/usr/bin/python3

'''a function that adds a new attribute to an object if it’s possible'''


def add_attribute(obj, attri, value):
    '''a function that adds a new attribute to an object if it’s possible'''
    if not hasattr(obj, '__dict__'):
        raise TypeError("nan't add new attribute")
    setattr(obj, attri, value)

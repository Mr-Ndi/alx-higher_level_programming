#!/usr/bin/pyton3
"""returing the dictionary description with simple data structure"""


def class_to_json(obj):
    """a function t0 return dictionary description and simple data structure"""
    return obj.__dict__

#!/usr/bin/python3
"""
A function that calculate the sum of 2 integers
Float arguments are type casted into integers before perfoming the operator
if b or a is not a number means not integer or not a float type error is raised
"""


def add_integer(a, b=98):
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

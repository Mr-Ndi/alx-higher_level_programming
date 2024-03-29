#!/usr/bin/python3
"""
a class definition based on 1
"""


class Square:
    """definiton of the square"""
    def __init__(self, size=0):
        """initialising"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

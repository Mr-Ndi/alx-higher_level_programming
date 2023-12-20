#!/usr/bin/python3
"""
a class for a simple siquare
"""


class Square:
    """class definition"""
    def __init__(self, size=0):
        """initialisation"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

#!/usr/bin/python3
"""
a class for a simple siquare
"""


class Square:
    """class definition"""
    def __init__(self, size=0):
        """initialisation"""
        self.size = size

    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def size(self):
        return self.size

    def area(self):
        """returning the area of the square"""
        return self.size ** 2

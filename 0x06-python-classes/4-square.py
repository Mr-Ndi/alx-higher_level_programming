#!/usr/bin/python3
"""
A simple class
"""


class Square:
    """Class containing the size attribute"""
    def __init__(self, size=0):
        """initiator function"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """setter of Square class"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """compute the area of the square"""
        return (self.__size)**2
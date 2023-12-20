#!/usr/bin/python3
"""
A simple class
"""


class Square:
    """Class containing the size attribute"""
    def __init__(self, size=0, position=(0, 0)):
        """initiator function"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, pos):
        if type(pos) != tuple or len(pos) != 2 or \
                not all([type(i) == int for i in pos]) or \
                not all([i >= 0 for i in pos]):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = pos

    def area(self):
        """compute the area of the square"""
        return (self.__size)**2

    def my_print(self):
        """print a square using the '#' character"""
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
        if self.__size == 0:
            print()

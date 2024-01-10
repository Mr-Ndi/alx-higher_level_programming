#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherted the basegeometry class"""

    def __init__(self, width, height):
        """Initialiser that initialise an instance of a class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """A function to imprement the area"""
        rn = self.__width * self.__height
        return rn

    def __str__(self):
        """Returning the following rectangle description"""
        ans = "[" + str(self.__class__.__name__) + "]"
        ans += str(self.__width) + "/" + str(self.__height)
        return ans

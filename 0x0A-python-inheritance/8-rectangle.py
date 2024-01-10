#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class that inherted the basegeometry class"""

    def __init__(self, width, height):
        """Initialiser that initialise an instance of a class"""
        self.integer_validator("width", width)
        self.__width = self
        self.integer_validator("height", height)
        self.__height = self

#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int) or value <= 0:
            raise TypeError("{} must be an integer".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = self 
        self.integer_validator("height", height)
        self.__height = self 

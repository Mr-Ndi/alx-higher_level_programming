#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        '''Setting up the value and width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        '''Setting up the value and height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''for displaying the area'''
        return self.__width * self.__height

    def perimeter(self):
        '''a function for returning the perimeter'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        '''function to create a rectangle'''
        if self.__width == 0 or self.__height == 0:
            return ('')
        poli = [
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        ]
        return '\n'.join(poli)

    def print(self):
        '''for displaying the created rectangle'''
        print(str(self))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raiseTypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raiseTypeError("rect_2 must be an instance of Rectangle")
        if rect_1 == rect_2:
            return rect_1
        result = rect_1 if rect_1.area() > rect_2.area() else rect_2
        return result

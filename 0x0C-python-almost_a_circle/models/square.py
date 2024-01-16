#!/usr/bin/python3

from models.rectangle import Rectangle


class Base:
    """ this is the base class that we are gonna use in
    this overall project about python
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ constructor for ID of class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """ public method that assigns attributes"""
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        else:
            if len(args) == 0:
                pass
            for opt, tipo in kwargs.items():
                setattr(self, opt, tipo)

    def to_dictionary(self):
        """Public method that returns the dictionary"""
        return {
            "id": self.id,
            "width": self.width,
            "x": self.x,
            "y": self.y,
        }

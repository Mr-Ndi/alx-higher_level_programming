#!/usr/bin/python3


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor"""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """for initialising the new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if not None and isinstance(attrs, list):
            return [elem for elem in attrs]
        return self.__dict__

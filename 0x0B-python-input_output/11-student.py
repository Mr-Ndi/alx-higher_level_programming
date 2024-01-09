#!/usr/bin/python3
"""class Student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """for initialising the new instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieving a dictionary
        representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        else:
            a = {}
            for attr in attrs:
                if hasattr(self, attr):
                    a[attr] = getattr(self, attr)
            return a

    def reload_from_json(self, json):
        for k in json:
            setattr(self, k, json[k])

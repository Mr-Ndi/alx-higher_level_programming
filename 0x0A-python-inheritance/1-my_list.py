#!/usr/bin/python3
"""a class MyList"""


class MyList(list):
    """method that prints the list, but sorted"""
    def print_sorted(self):
        p = sorted(self)
        print(p)

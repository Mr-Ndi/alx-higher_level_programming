#!/usr/bin/python3
"""the beginig of the project and this
    will focus on the file
"""
def read_file(filename=""):
    """ a function to read the file content"""
    with open(filename) as p:
        cont = p.read()
    print(cont, end="")

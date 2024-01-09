#!/usr/bin/python3
def read_file(filename=""):
    """ a function top read the file content"""
    with open(filename) as p:
        cont = p.read()
        print(cont, end="")

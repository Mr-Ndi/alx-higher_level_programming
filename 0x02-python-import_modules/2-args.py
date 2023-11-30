#!/usr/bin/python3
if __name__ == "__main__":
    """a program that prints the number of and the list of its arguments"""
    import sys


    length = len(sys.argv) - 1
    if length == 0:
        print("{} arguments.".format(length))
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[length]))
    else:
        print("{} arguments:".format(length))
        for i in range(1, length + 1):
            print("{}: {}".format(i, sys.argv[i]))

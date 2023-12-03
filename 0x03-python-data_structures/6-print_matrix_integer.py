#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for k in i:
            print("{:d}".format(k), end=' ')
        print()

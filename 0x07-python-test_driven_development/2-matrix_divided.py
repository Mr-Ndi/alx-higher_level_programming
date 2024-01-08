#!/usr/bin/python3
def matrix_divided(matrix, div):
    if not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for lis in matrix:
        if not isinstance(lis, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(lis) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for element in lis:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(div) not in [int, float]:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
    if not all(len(lis) == len(matrix[0]) for lis in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return[[round(element / div, 2) for element in lis] for lis in matrix]

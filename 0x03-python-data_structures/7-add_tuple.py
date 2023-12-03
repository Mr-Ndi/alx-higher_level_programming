#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = []
    for i in range(2):
        if i >= len(tuple_a):
            num_1 = 0
        else:
            num_1 = tuple_a[i]
        if i >= len(tuple_b):
            num_2 = 0
        else:
            num_2 = tuple_b[i]
        result.append(num_1 + num_2)
    return tuple(result)

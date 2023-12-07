#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    product = map(lambda p: p * number, my_list)
    final = list(product)
    return final

#!/usr/bin/python3
def weight_average(my_list=[]):
    prod = 0
    val = 0
    if not my_list:
        return 0
    for i in my_list:
        prod += i[0] * i[1]
        val += i[1]
    return prod / val

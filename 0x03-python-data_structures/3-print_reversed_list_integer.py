#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ingano = len(my_list)
    for ele in range(ingano - 1, -1, -1):
        print("{:d}".format(my_list[ele]))

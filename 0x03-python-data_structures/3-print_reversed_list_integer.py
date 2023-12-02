#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for ele in my_list:
        ele *= -1
        print("{:d}".format(my_list[ele]))
        ele *= -1

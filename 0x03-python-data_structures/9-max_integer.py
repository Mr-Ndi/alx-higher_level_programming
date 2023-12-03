#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        maximum = my_list[0]
        for elem in my_list:
            if elem > maximum:
                maximum = elem
        return maximum

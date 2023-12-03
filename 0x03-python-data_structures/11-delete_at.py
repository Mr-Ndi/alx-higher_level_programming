#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < length and idx >= 0:
        del my_list[idx]
    else:
        return my_list
    return my_list

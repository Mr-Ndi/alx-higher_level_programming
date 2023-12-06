#!/usr/bin/python3
def search_replace(my_list, search, replace):

    leng = len(my_list)
    newone = my_list.copy()
    for i in range(leng):
        if newone[i] == search:
            newone[i] = replace
    return newone

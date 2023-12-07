#!/usr/bin/python3
def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    else:
        init = list(a_dictionary)
        begin = init[0]
        for ii in init:
            if a_dictionary[ii] > a_dictionary[begin]:
                begin = ii
        return begin

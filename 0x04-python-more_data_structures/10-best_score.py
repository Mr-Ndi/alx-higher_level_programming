#!/usr/bin/python3
def best_score(a_dictionary):

    init = a_dictionary{0}
    for ii in a_dictionary:
        curr = a_dictionary.get(ii)
        if curr is not None:
            if curr > init:
                init = curr
    return init

#!/usr/bin/python3
def best_score(a_dictionary):

    init = list(a_dictionary.values())

    if not init:
        return None
    begin = init[0]
    for ii in init:
        if ii > begin:
            begin = ii
    return begin

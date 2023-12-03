#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        my_tuple = (0, 'None')
    else:
        fchar = sentence[0]
        my_tuple = (leng, fchar)
    return my_tuple

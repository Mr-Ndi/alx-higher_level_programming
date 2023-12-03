#!/usr/bin/python3
def multiple_returns(sentence):
    leng = len(sentence)
    if leng == 0:
        my_tuple = (0, 'None')
    else:
        my_tuple = (leng, 'sentence[0]')
    return my_tuple

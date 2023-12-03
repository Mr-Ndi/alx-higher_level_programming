#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ans = my_list.copy()
    leng = len(my_list)
    for elem in range(leng - 1):
        if elem % 2 == 0:
            ans[elem] = True
        else:
            ans[elem] = False
    return ans

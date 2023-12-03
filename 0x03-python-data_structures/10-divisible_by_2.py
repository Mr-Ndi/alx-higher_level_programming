#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    else:
        ans = my_list.copy()
        leng = len(my_list)
        for elem in range(leng - 1):
            if my_list[elem] % 2 == 0:
                ans[elem] = True
            else:
                ans[elem] = False
        return ans

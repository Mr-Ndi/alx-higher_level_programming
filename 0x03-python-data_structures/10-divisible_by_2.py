#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    else:
        ans = []
        for elem in my_list:
            if elem % 2 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

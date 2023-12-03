#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list == []:
        return None
    else:
        ans = [] 
        leng = len(my_list)
        for elem in range(leng - 1):
            if my_list[elem] % 2 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

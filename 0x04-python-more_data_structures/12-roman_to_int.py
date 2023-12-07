#!/usr/bin/python3
def roman_to_int(roman_string):
    ans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    cont = list(roman_string)
    num = 0
    p = 0
    while p < len(cont):
        if p != len(cont) - 1 and ans[cont[p]] < ans[cont[p + 1]]:
            num += ans[cont[p + 1]] - ans[cont[p]]
            p += 2
        else:
            num += ans[cont[p]]
            p += 1
    return num

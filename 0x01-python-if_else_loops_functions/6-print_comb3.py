#!/usr/bin/python3
for k1 in range(0, 10):
    for k2 in range(1, 10):
        if k1 >= k2:
            continue
        elif k1 == 8 and k2 == 9:
            print("{}{}".format(k1, k2))
        else:
            print("{}{}".format(k1, k2), end=", ")

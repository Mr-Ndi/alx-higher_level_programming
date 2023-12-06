#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    differ1_2 = set_1 - set_2
    differ2_1 = set_2 - set_1
    common = differ1_2 | differ2_1
    return common

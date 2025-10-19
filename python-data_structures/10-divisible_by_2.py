#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    res = []
    for n in my_list:
        res.append(n % 2 == 0)
    return res

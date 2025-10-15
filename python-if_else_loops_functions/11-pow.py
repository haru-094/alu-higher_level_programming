#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    elif b > 0:
        res = 1
        for _ in range(b):
            res *= a
        return res
    else:
        res = 1
        for _ in range(-b):
            res *= a
        return 1 / res

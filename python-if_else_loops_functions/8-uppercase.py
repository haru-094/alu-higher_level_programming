#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            res += "{}".format(chr(ord(c) - 32))
        else:
            res += "{}".format(c)
    print(res)

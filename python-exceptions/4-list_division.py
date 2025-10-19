#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    res = []
    for i in range(list_length):
        try:
            num = my_list_1[i]
            den = my_list_2[i]
            if not isinstance(num, (int, float)) or not isinstance(den, (int, float)):
                print("wrong type")
                res.append(0)
                continue
            try:
                div = num / den
            except ZeroDivisionError:
                print("division by 0")
                div = 0
            res.append(div)
        except IndexError:
            print("out of range")
            res.append(0)
    return res

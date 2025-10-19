#!/usr/bin/python3
def multiple_by_2(a_dictionary):
    newDict = {}
    for key, value in a_dictionary.items():
        newDict[key] = value * 2
    return newDict

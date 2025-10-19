#!/usr/bin/python3
def roman_to_int(roman_string):
    return 0 if not isinstance(roman_string, str) or roman_string is None else sum(-{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}[c] if i+1<len(roman_string) and {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}[c]<{'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}[roman_string[i+1]] else {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}[c] for i,c in enumerate(roman_string))

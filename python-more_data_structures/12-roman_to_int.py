#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string == None or not isinstance(roman_string, str):
        return 0
    dic_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500,'M': 1000}
    number  = 0
    for i in range(0, len(roman_string)):
        if len(roman_string) == 1:
            number = dic_roman[roman_string[i]]
        elif dic_roman[roman_string[i - 1]] < dic_roman[roman_string[i]] and i != 0:
            number += (dic_roman[roman_string[i]]) - (dic_roman[roman_string[i - 1]] * 2)
        else:
            number += dic_roman[roman_string[i]]
    return number

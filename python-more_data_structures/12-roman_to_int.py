#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    d_r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for i in range(0, len(roman_string)):
        if len(roman_string) == 1:
            number = d_r[roman_string[i]]
        elif d_r[roman_string[i - 1]] < d_r[roman_string[i]] and i != 0:
            number += (d_r[roman_string[i]]) - (d_r[roman_string[i - 1]] * 2)
        else:
            number += d_r[roman_string[i]]
    return number

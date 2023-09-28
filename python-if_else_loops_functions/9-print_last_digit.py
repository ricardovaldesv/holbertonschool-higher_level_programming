#!/usr/bin/python3
def print_last_digit(number):
    n_str = str(number)
    last_digit = n_str[-1]
    print("{}".format(last_digit), end='')
    return last_digit

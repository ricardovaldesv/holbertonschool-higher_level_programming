#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value is None:
            return 0
        else:
            print('{:d}'.format(value))
            return True
    except ValueError:
        return False

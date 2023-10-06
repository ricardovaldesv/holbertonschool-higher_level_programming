#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        if my_list is None or x is 0:
            return 0
        else:
            for i in range(x):
                print('{}'.format(my_list[i]), end='')
    except IndexError:
        return i
    else:
        return i + 1
    finally:
        print('')

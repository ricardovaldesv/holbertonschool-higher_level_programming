#!/usr/bin/python3
def uppercase(str):

    lenght = len(str)
    for i in range(0, lenght):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            c = chr(ord(str[i]) - 32)
        else:
            c = str[i]
        print("{}".format(c), end='')
    print("{}".format("\n"), end='')

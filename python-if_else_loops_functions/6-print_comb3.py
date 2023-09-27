#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(1, 10):
        if num2 <= num1:
            continue
        if (num1 * 10 + num2) == 89:
            print("{:02}".format(num1 * 10 + num2))
        else:
            print("{:02}, ".format(num1 * 10 + num2), end='')

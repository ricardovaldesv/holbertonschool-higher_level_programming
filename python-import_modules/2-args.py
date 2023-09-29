#!/usr/bin/python3

import sys


def func():
    arguments = len(sys.argv)
    if arguments == 2:
        print("{0} {1}".format(arguments - 1, 'argument:'))
    else:
        print("{0} {1}".format(arguments - 1, 'arguments:'))

    for i in range(1, arguments):
        print("{0}: {1}".format(i, sys.argv[i]))


if __name__ == "__main__":
    func()

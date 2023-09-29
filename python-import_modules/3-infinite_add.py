#!/usr/bin/python3

import sys


def infinite_add():
    arguments = len(sys.argv)
    result = 0

    for i in range(1, arguments):
        result += int(sys.argv[i])
    print("{}".format(result))


if __name__ == "__main__":
    infinite_add()

#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        file1 = file.read()
        for line in file1:
            print(line, end='')

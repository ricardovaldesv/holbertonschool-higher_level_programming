#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    matrix = sorted(a_dictionary.items())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j == len(matrix[i]) - 1:
                print('{}'.format(matrix[i][j]))
            else:
                print('{}: '.format(matrix[i][j]), end='')

#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    flag = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j == len(matrix[0]) - 1:
                print('{}'.format(matrix[i][j]))
            else:
                print('{} '.format(matrix[i][j]), end='')
            flag = 1
    if flag == 0:
        print('{}'.format(''))

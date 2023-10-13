#!/usr/bin/python3
"""
Function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.
    """

    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")

    for i in range(len(matrix)):
        if i < len(matrix) - 1:
            if len(matrix[i]) != len(matrix[i + 1]):
                raise TypeError("Each row of the matrix must"
                                " have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_row = []
        for j in range(len(matrix[i])):
            number = matrix[i][j] / div
            digit = round(number, 2)
            new_row.append(digit)
        new_matrix.append(new_row)
    return new_matrix

#!/usr/bin/python3
"""This module contains a function called pascal_triangle"""


def pascal_triangle(n):
    """pascal_triangle returns a list of lists representinf pascal
    triangle

    Args:
        n (int): n pascal triangle
    """
    pascal = []
    if n > 0:
        prev = []
        for i in range(n):
            level = []
            if i == 0:
                level.append(1)
            elif i == 1:
                level.append(1)
                level.append(1)
                prev.append(1)
                prev.append(1)
            else:
                level.append(1)
                j = 0
                while j < len(prev) - 1:
                    level.append(prev[j] + prev[j + 1])
                    j += 1
                level.append(1)
                if i >= 2:
                    prev = []
                    for k in level:
                        prev.append(k)
            pascal.append(level)
        return pascal
    return pascal

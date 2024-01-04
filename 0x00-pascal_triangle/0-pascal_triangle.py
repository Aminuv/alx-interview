#!/usr/bin/python3

"""
    The Module for working with Pascal's triangle.
"""


def pascal_triangle(n):

    """
        To creates a list of lists for integers represent
    Pascal triangle of  given integer.
    """
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for m in range(n):
        line = []
        for j in range(m + 1):
            if j == 0 or j == m:
                line.append(1)
            elif m > 0 and j > 0:
                line.append(triangle[m - 1][j - 1] + triangle[m - 1][j])
        triangle.append(line)
    return triangle

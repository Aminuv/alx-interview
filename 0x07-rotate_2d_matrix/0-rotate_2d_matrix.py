#!/usr/bin/python3
"""The 2D Rotate of Matrix"""


def rotate_2d_matrix(matrix):
    """ Rotates a 2D Matrix 90° clockwise """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    matrix[:] = [row[::-1] for row in matrix]

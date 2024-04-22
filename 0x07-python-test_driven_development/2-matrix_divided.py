#!/usr/bin/python3
""" matrix divided module"""


def matrix_divided(matrix, div):
    matrix1 = matrix[0, 0] / div
    matrix.append(matrix1)
    return matrix
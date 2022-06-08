#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    square = []
    row = []
    for i in matrix:
        for j in i:
            row.append(j * j)
        square.append(row)
        row = []
    return square

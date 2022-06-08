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


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)

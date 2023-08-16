#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            square = element ** 2
            new_row.append(square)
        new_matrix.append(new_row)
    return new_matrix
    print("{}".format(new_matrix))
    print("{}".format(matrix))

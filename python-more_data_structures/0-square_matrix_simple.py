#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        new_row = [i ** 2 for i in r]
        new_matrix.append(new_row)
    return new_matrix

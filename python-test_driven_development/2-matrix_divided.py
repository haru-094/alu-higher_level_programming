#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    matrix must be a list of lists of integers or floats,
    otherwise raise TypeError with message:
    "matrix must be a matrix (list of lists) of integers/floats"
    Returns a new matrix with elements divided by div rounded to 2 decimals.
    """
    if not (isinstance(matrix, list) and all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0]) if matrix else 0
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(elem / div, 2) for elem in row]
        new_matrix.append(new_row)

    return new_matrix

#!/usr/bin/python3
"""
This module provides a function for dividing all elements of a matrix.

The module contains the matrix_divided function which divides all elements
of a matrix by a given divisor and returns a new matrix with results
rounded to 2 decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats
        div: The divisor (int or float), cannot be 0

    Returns:
        list: A new matrix with all elements divided by div,
              rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of the matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0

    Examples:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
        >>> matrix_divided([[10, 20]], 2)
        [[5.0, 10.0]]
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

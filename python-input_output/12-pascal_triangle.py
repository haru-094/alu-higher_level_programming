#!/usr/bin/python3
"""
Create function pascal_triangle
"""


def pascal_triangle(n):
    """
    return a list integer
    """
    if n <= 0:
        return []
    triangle = [[1]]

    for i in range(1, n):
        p_row = triangle[-1]
        n_row = [1]

        for j in range(1, len(p_row)):
            n_row.append(p_row[j - 1] + p_row[j])
        n_row.append(1)
        triangle.append(n_row)

    return triangle

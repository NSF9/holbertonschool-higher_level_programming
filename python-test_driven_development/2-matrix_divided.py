#!/usr/bin/python3
"""
This module defines the matrix_divided function which divides elements
of a matrix by a number and returns a new matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number (div).

    Args:
        matrix (list of lists): A matrix containing integers or floats.
        div (int or float): The number to divide by.

    Returns:
        list of lists: A new matrix with elements divided and rounded to 2
        decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of numbers.
        TypeError: If rows of the matrix are not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

            new_row.append(round(value / div, 2))

        new_matrix.append(new_row)

    return new_matrix

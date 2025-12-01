#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join(str(row) for row in row), end="$")
        print()

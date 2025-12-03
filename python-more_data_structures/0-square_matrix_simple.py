#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == []:
     return matrix

    new_list = [] 
    for row in matrix:
        new_row = []
        for number in row:
            new_row.append(number ** 2)
        new_list.append(new_row)

    return new_list

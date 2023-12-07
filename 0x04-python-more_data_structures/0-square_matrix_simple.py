#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = list(map(lambda row: [x ** 2 for x in row], matrix))
    return result

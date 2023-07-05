#!/usr/bin/python3

"""
This module divides a matrix (List of Lists) by a given number
and then returns a new matrix (List of Lists) with the answers
to the division
"""


def matrix_divided(matrix, div):
    """
    This function calculates the division of a matrix by div.
    Div must be a number greater than 0 and must be an int
    else an error is thrown

    Matrix cannont be any other thing except an int
    """
    verify_len = []
    newlist = list()
    index = 0
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    if type(div) != int:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix[0]) != list:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    elif len(matrix) < 1:
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    else:
        for val in matrix:
            verify_len.append(len(val))
        if len(set(verify_len)) != 1:
            raise TypeError("Each row of the matrix must have the same size")
        else:
            for arr in matrix:
                newlist.append(list())
                for val in arr:
                    if type(val) != int:
                        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
                    else:
                        newlist[index].append(round(val/div, 2))
                index += 1
        return newlist

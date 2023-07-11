#!/usr/bin/python3

"""
This is a module that contains a function def pascal_triangle(n):
that returns a list of lists of integers representing the Pascal`s

=> You can assume n will be always an integer
=> You are not allowed to import any module
"""


def pascal_triangle(n):
    """
    This returns a pascal triangle of n length
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

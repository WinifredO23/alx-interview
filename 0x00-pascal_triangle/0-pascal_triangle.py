#!/usr/bin/python3
"""
Module to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle up to row n.

    Args:
        n (int): The number of rows of the triangle.

    Returns:
        List of lists of integers representing Pascal’s triangle.
    """
    if n <= 0:
        return []

    triangle = []  # Initialize an empty list to store the triangle

    for i in range(n):
        row = [1] * (i + 1)

        # Calculate the middle values, if applicable
        for j in range(1, i):
            row[j] = (triangle[i - 1][j - 1] +
                      triangle[i - 1][j])

        triangle.append(row)  # Add the row to the triangle
    return triangle

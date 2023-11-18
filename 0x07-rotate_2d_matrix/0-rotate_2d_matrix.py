#!/usr/bin/python3

"""Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """


def rotate_2d_matrix(matrix):
    """Rotates a 2D matrix

    Args:
        matrix: 2D matrix
    """
    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append([])
        for j in range(len(matrix[i])):
            new_matrix[i].append(matrix[-1 - j][i])

    matrix[:] = new_matrix

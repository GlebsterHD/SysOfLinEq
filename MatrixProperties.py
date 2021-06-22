from typing import List, Union

import MatrixExceptions as me

Matrix = List[list]


def is_square(matrix: Matrix):
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            raise me.MatrixIsNotSquare


def is_numeric(matrix: Matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int or float):
                raise me.MatrixIsNotNumeric


def is_vec_numeric(vector: list):
    for i in range(len(vector)):
        if not isinstance(vector[i], int or float):
            raise me.VectorIsNotNumeric


def is_matrix(matrix: Matrix):
    for i in range(1, len(matrix)):
        if len(matrix[i]) != len(matrix[i - 1]):
            raise me.ListIsNotMatrix


def is_numeric_matrix(matrix: Matrix):
    is_numeric(matrix)
    is_matrix(matrix)


def is_det_calculable(matrix: Matrix):
    is_numeric_matrix(matrix)
    is_square(matrix)


def are_multipliable(matrix: Matrix, vec: list):
    is_numeric_matrix(matrix)
    is_vec_numeric(vec)

    for i in range(len(matrix)):
        if len(matrix[i]) != len(vec) or not is_numeric_matrix(matrix):
            raise me.MatrixAndVectorNotMultipliable


def is_determinant_zero(det: Union[int, float]):
    if det == 0:
        raise me.MatrixDeterminantIsZero

import copy
from typing import List, Union

Matrix = List[list]


def calc_determinant(matrix: Matrix) -> Union[int, float]:
    # TODO: Add a check for square shape
    if len(matrix) == 1:
        return matrix[0][0]

    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    total = 0
    minors = get_minors_of_i_row(matrix, 0)
    for j in range(len(matrix)):
        total += matrix[0][j] * minors[j] * get_sign(0, j)

    return total


def get_minor(matrix: Matrix, line_number: int, column_number: int) -> Union[int, float]:
    minor = [row[:column_number] + row[column_number + 1:] for row in (matrix[:line_number] + matrix[line_number:])]
    return calc_determinant(minor)


def get_minors_of_i_row(matrix: Matrix, line_number: int):
    minors = []
    for j in range(len(matrix)):
        minors.append(get_minor(matrix, line_number, j))
    return minors


def get_matrix_of_minors(matrix: Matrix):
    a = []
    for i in range(len(matrix)):
        a.append(get_minors_of_i_row(matrix, i))
    return a


def get_sign(i, j):
    return (-1) ** (i + j)


def get_adj_matrix(matrix: Matrix):
    return [[get_sign(i, j) * get_matrix_of_minors(matrix)[j][i] for i in range(len(matrix))] for j in
            range(len(matrix))]


def get_invert_matrix(matrix: Matrix):
    det = calc_determinant(matrix)
    return multiply_by_num(get_adj_matrix(transpose_matrix(matrix)), 1 / det)


def swap_indexes(matrix: Matrix, i, j):
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def transpose_matrix(matrix: Matrix):
    m2 = copy.deepcopy(matrix)
    for i in range(0, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            swap_indexes(m2, j, i)
    return m2


def multiply_by_vec(matrix: Matrix, vector: list) -> list:
    # TODO: Написать исключение про разную длину вектора и матрицы
    m = []
    for i in range(len(vector)):
        total = 0
        for j in range(len(vector)):
            total += matrix[i][j] * vector[j]
        m.append(total)
    return m


def multiply_by_num(matrix, number):
    return [number * row[i] for row in matrix for i in range(len(row))]

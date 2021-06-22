import copy
from typing import List, Union
import MatrixExceptions as Me
import MatrixProperties as Mp

Matrix = List[list]


def calc_determinant(matrix: Matrix) -> Union[int, float, None]:
    try:
        Mp.is_det_calculable(matrix)
    except Me.MatrixException as exc:
        print(exc)
        return

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
    minor = [row[:column_number] + row[column_number + 1:] for row in (matrix[:line_number] + matrix[line_number + 1:])]
    return calc_determinant(minor)


def get_minors_of_i_row(matrix: Matrix, line_number: int) -> list:
    minors = []
    for j in range(len(matrix)):
        minors.append(get_minor(matrix, line_number, j))
    return minors


def get_matrix_of_minors(matrix: Matrix) -> Matrix:
    a = []
    for i in range(len(matrix)):
        a.append(get_minors_of_i_row(matrix, i))
    return a


def get_sign(i: int, j: int) -> int:
    return (-1) ** (i + j)


def get_adj_matrix(matrix: Matrix) -> Matrix:
    return [[get_sign(i, j) * get_matrix_of_minors(matrix)[j][i] for i in range(len(matrix))]
            for j in range(len(matrix))]


def get_invert_matrix(matrix: Matrix) -> Matrix:
    det = calc_determinant(matrix)
    try:
        Mp.is_determinant_zero(det)
    except Me.MatrixException as exc:
        print(exc)
    return multiply_by_num(get_adj_matrix(transpose_matrix(matrix)), 1 / det)


def swap_indexes(matrix: Matrix, i: int, j: int):
    try:
        Mp.is_square(matrix)
    except Me.MatrixException as exc:
        print(exc)
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def transpose_matrix(matrix: Matrix) -> Matrix:
    try:
        Mp.is_matrix(matrix)
    except Me.MatrixException as exc:
        print(exc)

    m = copy.deepcopy(matrix)
    m2 = []
    for j in range(len(matrix[0])):
        line = []
        for i in range(len(matrix)):
            line.append(m[i][j])
        m2.append(line)
        return m2


def multiply_by_vec(matrix: Matrix, vector: list) -> list:
    try:
        Mp.are_multipliable(matrix, vector)
    except Me.MatrixException as exc:
        print(exc)

    m = []
    for i in range(len(vector)):
        total = 0
        for j in range(len(vector)):
            total += matrix[i][j] * vector[j]
        m.append(total)
    return m


def multiply_by_num(matrix: Matrix, number: Union[int, float]) -> Matrix:
    try:
        Mp.is_numeric_matrix(matrix)
    except Me.MatrixException as exc:
        print(exc)

    return [number * row[i] for row in matrix for i in range(len(row))]


c = [[1, 3, 5], [4, 3, 4], [4, 5.3434, 34]]
calc_determinant(c)

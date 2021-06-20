import copy
from typing import List


class Matrix:
    #Describes matrices and their functions

def __init__(self, matrix : List[list], name : str = "a" ):
    self.name = name
    self.matrix = matrix



def calc_determinant(a):
    if len(a) == 1:
        if isinstance(a[0], int):
            return a[0]
        else:
            return a[0][0]

    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]

    total = 0
    minors = get_minors_of_i_row(a, 0)

    for j in range(len(a)):
        total += a[0][j] * minors[j] * get_sign(0, j)

    return total


def get_minors_of_i_row(matrix, line_number):
    minors = []
    for j in range(len(matrix)):
        c = []
        for i in range(len(matrix)):
            if i == line_number:
                continue
            b = []
            for k in range(len(matrix)):
                if k == j:
                    continue
                b.append(matrix[i][k])
            c.append(b)
        minors.append(calc_determinant(c))
    return minors


def get_minors_of_i_row2(matrix, line_number):
    # почему-то работает медленнее (примерно на 15%), чем ее первая версия
    minors = []
    for j in range(len(matrix)):
        b = [[matrix[i][k] for i in range(len(matrix)) if i != line_number] for k in range(len(matrix)) if k != j]
        minors.append(calc_determinant(b))
    return minors


def get_matrix_of_minors(matrix):
    a = []
    for i in range(len(matrix)):
        a.append(get_minors_of_i_row(matrix, i))
    return a


def get_sign(i, j):
    return (-1) ** (i + j)


def get_adj_matrix(matrix):
    return [[get_sign(i, j) * get_matrix_of_minors(matrix)[j][i] for i in range(len(matrix))] for j in
            range(len(matrix))]


def get_invert_matrix(matrix):
    det = calc_determinant(matrix)
    return multiply_by_num(get_adj_matrix(transpose_matrix(matrix)), 1 / det)


def swap_indexes(matrix, i, j):
    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def transpose_matrix(matrix):
    m2 = copy.deepcopy(matrix)
    for i in range(0, len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            swap_indexes(m2, j, i)
    return m2

def multiply_by_vec(matrix, vector):
    m = []
    for i in range(len(vector)):
        total = 0
        for j in range(len(vector)):
            total += matrix[i][j] * vector[j]
        m.append(total)
    return m

def multiply_by_num(matrix, number):
    a = []
    for i in range(len(matrix)):
        b= []
        for j in range(len(matrix)):
            b. append(matrix[i][j] * number)
        a.append(b)
    return a
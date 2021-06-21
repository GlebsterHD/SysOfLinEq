from typing import List


Matrix = List[list]


def is_square(matrix: Matrix) -> bool:
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return False
    return True


def is_numeric(matrix: Matrix) -> bool:
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int or float):
                return False
    return True

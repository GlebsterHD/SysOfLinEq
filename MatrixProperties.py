from typing import List


Matrix = List[list]


def is_square(matrix: Matrix) -> bool:
    for i in range(len(matrix)):
        if len(matrix[i]) != len(matrix):
            return False
    return True

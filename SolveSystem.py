import MatrixOperations as mo


def solve_by_kramer(matrix, vector):
    det = mo.calc_determinant(matrix)
    # Todo: Add an exception for det = 0
    if det == 0:
        return "определитель системы равен 0"

    d = []
    for k in range(len(matrix)):
        c = []
        for i in range(len(matrix)):
            b = []
            for j in range(len(matrix)):
                if j == k:
                    b.append(vector[i])
                else:
                    b.append(matrix[i][j])
            c.append(b)
        d.append(mo.calc_determinant(c) / det)
    return d


def solve_by_matrices(matrix, vector):
    return mo.multiply_by_vec(mo.get_invert_matrix(matrix), vector)

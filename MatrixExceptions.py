class MatrixException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None

    def __str__(self):
        return f"Error: {self.msg}"


class MatrixIsNotSquare(MatrixException):
    def __str__(self):
        return "Error: Matrix is not square"


class MatrixIsNotNumeric(MatrixException):
    def __str__(self):
        return "Error: Matrix contains not numeric values"


class VectorIsNotNumeric(MatrixException):
    def __str__(self):
        return "Error: Vector contains not numeric values"


class ListIsNotMatrix(MatrixException):
    def __str__(self):
        return "Error: List has different length of lines"


class MatrixAndVectorNotMultipliable(MatrixException):
    def __str__(self):
        return "Error: Matrix and vector have different dimensions"


class MatrixDeterminantIsZero(MatrixException):
    def __str__(self):
        return "Error: Matrix determinant is zero"

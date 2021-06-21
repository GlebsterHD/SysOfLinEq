from typing import List
import MatrixExceptions


class Matrix:
    def __init__(self, matrix: List[list], name: str = "a"):
        # TODO: check for values in lists
        self.name = name
        self.matrix = matrix

    Matrix = List[list]
# TODO: add a print function

    @property
    def __len__(self) -> int:
        return len(self.matrix)

    def __getitem__(self, item) -> list:
        return self.matrix[item]

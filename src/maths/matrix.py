from typing import List, Union

from maths.utils import is_matrix_mutiplicable


class Matrix:
    def __init__(self):
        pass

    @staticmethod
    def multiply(matrix_A: List[Union[int, float]], matrix_B: List[Union[int, float]]):
        """Regular Matrix multiplication
        A_rows x A_cols * B_rows x B_cols = A_rows x B_cols

        T: O(nmk), n = len(A_rows); m = len(A_cols); k = len(B_cols)
        """

        if is_matrix_mutiplicable(matrix_A=matrix_A, matrix_B=matrix_B):
            A_cols = len(matrix_A[0])
            A_rows = len(matrix_A)
            B_cols = len(matrix_B[0])

            C = [[0] * B_cols for _ in range(A_rows)]

            for rA in range(A_rows):
                for cB in range(B_cols):
                    for rBcA in range(A_cols):
                        C[rA][cB] += matrix_A[rA][rBcA] * matrix_B[rBcA][cB]
            return C
        return []

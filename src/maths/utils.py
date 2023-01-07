from typing import List, Union


def is_matrix_mutiplicable(
    matrix_A: List[Union[int, float]], matrix_B: List[Union[int, float]]
):
    """Check if two matrixes can multiply"""
    return len(matrix_A[0]) == len(matrix_B)

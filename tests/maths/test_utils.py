from typing import List, Union

import pytest

from maths.utils import is_matrix_mutiplicable


@pytest.mark.parametrize(
    "matrix_A,matrix_B,expected",
    [
        (
            [[0, 2, 0], [0, -3, 5]],
            [[0, 10, 0], [0, 0, 0], [0, 0, 4]],
            True,
        ),
        (
            [[46, 0, 0], [45, 47, 0], [0, 0, 0], [34, 0, 25], [0, 2, 0], [0, 0, 0]],
            [[26, 34, 20, 31, 34, 15], [38, 30, 23, 1, 45, 22], [47, 9, 9, 5, 9, 31]],
            True,
        ),
        (
            [[0, 2, 0], [0, -3, 5]],
            [[1]],
            False,
        ),
    ],
)
def test_is_matrix_multiplicable(
    matrix_A: List[Union[int, float]], matrix_B: List[Union[int, float]], expected: bool
):
    assert is_matrix_mutiplicable(matrix_A=matrix_A, matrix_B=matrix_B) == expected

from typing import List, Union

import pytest

from maths.matrix import Matrix


@pytest.mark.parametrize(
    "matrix_A,matrix_B,expected",
    [
        (
            [[0, 2, 0], [0, -3, 5]],
            [[0, 10, 0], [0, 0, 0], [0, 0, 4]],
            [[0, 0, 0], [0, 0, 20]],
        ),
        (
            [[46, 0, 0], [45, 47, 0], [0, 0, 0], [34, 0, 25], [0, 2, 0], [0, 0, 0]],
            [[26, 34, 20, 31, 34, 15], [38, 30, 23, 1, 45, 22], [47, 9, 9, 5, 9, 31]],
            [
                [1196, 1564, 920, 1426, 1564, 690],
                [2956, 2940, 1981, 1442, 3645, 1709],
                [0, 0, 0, 0, 0, 0],
                [2059, 1381, 905, 1179, 1381, 1285],
                [76, 60, 46, 2, 90, 44],
                [0, 0, 0, 0, 0, 0],
            ],
        ),
        (
            [[0, 2, 0], [0, -3, 5]],
            [[1]],
            [],
        ),
    ],
)
def test_matrix_multiply(
    matrix_A: List[Union[int, float]],
    matrix_B: List[Union[int, float]],
    expected: List[Union[int, float]],
):
    assert Matrix.multiply(matrix_A=matrix_A, matrix_B=matrix_B) == expected

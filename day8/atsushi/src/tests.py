from unittest import mock

import pytest

from src import input, search

MATRIX = input.load("inputs/test.txt")


@pytest.mark.parametrize(
    "file, expected_answer", (("inputs/puzzle.txt", 201600), ("inputs/test.txt", 8))
)
def test_part2(file, expected_answer) -> None:
    grid = input.load(file)

    assert expected_answer == search.find_scenic_score(grid)


@pytest.mark.parametrize(
    "map, iter, cols, expected",
    (
        [
            MATRIX,
            1,
            False,
            [
                [0, 1, 2, 3, 1],
                [0, 1, 1, 1, 2],
                [0, 1, 1, 1, 1],
                [0, 1, 2, 1, 4],
                [0, 1, 1, 3, 1],
            ],
        ],
        [
            MATRIX,
            -1,
            False,
            [
                [2, 1, 1, 1, 0],
                [1, 1, 2, 1, 0],
                [4, 3, 1, 1, 0],
                [1, 1, 2, 1, 0],
                [1, 2, 1, 1, 0],
            ],
        ],
        [
            MATRIX.T,
            1,
            True,
            [
                [0, 0, 0, 0, 0],
                [1, 1, 1, 1, 1],
                [2, 1, 1, 2, 1],
                [1, 1, 2, 3, 3],
                [1, 2, 1, 4, 1],
            ],
        ],
        [
            MATRIX.T,
            -1,
            True,
            [
                [2, 1, 1, 4, 3],
                [1, 1, 2, 1, 1],
                [2, 2, 1, 1, 1],
                [1, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
            ],
        ],
    ),
)
def test_row_scenic_score(map, iter, cols, expected) -> None:
    actual = search.iter_map_2(map, iter, cols)

    assert expected == actual

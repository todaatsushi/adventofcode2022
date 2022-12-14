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

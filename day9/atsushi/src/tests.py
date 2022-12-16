import pytest

from src import data, input, move


@pytest.mark.parametrize(
    "old, new, expected",
    (
        (
            (1, 1),
            (0, 1),
            data.Direction.LEFT,
        ),
        (
            (1, 1),
            (2, 1),
            data.Direction.RIGHT,
        ),
        (
            (1, 1),
            (1, 2),
            data.Direction.UP,
        ),
        (
            (1, 1),
            (1, 0),
            data.Direction.DOWN,
        ),
    ),
)
def test_get_new_direction(
    old: data.Coordinate, new: data.Coordinate, expected: data.Direction
) -> None:
    res = data.get_new_direction(old, new)

    assert res == expected


@pytest.mark.parametrize(
    "file, tails, expected",
    (
        ("inputs/test.txt", 1, 13),
        ("inputs/puzzle.txt", 1, 6098),
        ("inputs/test.txt", 9, 1),
        ("inputs/puzzle.txt", 9, 0),
    ),
)
def test_day(file: str, tails: int, expected: int) -> None:
    directions = input.load(file)
    head = move.apply(directions, tails)

    t = head
    while t.tail:
        t = t.tail
    assert isinstance(t, data.Tail)

    assert len(t.visited) == expected

import pytest

from src import data, input, move


@pytest.mark.parametrize(
    "file, tails, expected",
    (
        ("inputs/test.txt", 1, 13),
        ("inputs/puzzle.txt", 1, 6098),
        ("inputs/test.txt", 9, 1),
        ("inputs/puzzle.txt", 9, 2597),
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


@pytest.mark.parametrize(
    "moves, tails, expected",
    (
        (
            ((data.Direction.UP, 1),),
            1,
            (
                (0, 1),
                (0, 0),
            ),
        ),
        (
            ((data.Direction.LEFT, 1),),
            1,
            (
                (-1, 0),
                (0, 0),
            ),
        ),
        (
            ((data.Direction.RIGHT, 1),),
            1,
            (
                (1, 0),
                (0, 0),
            ),
        ),
        (
            ((data.Direction.DOWN, 1),),
            1,
            (
                (0, -1),
                (0, 0),
            ),
        ),
        (
            ((data.Direction.RIGHT, 4),),
            1,
            (
                (4, 0),
                (3, 0),
            ),
        ),
        (
            ((data.Direction.DOWN, 10),),
            1,
            (
                (0, -10),
                (0, -9),
            ),
        ),
        (
            (
                (data.Direction.UP, 3),
                (data.Direction.RIGHT, 4),
            ),
            1,
            (
                (4, 3),
                (3, 3),
            ),
        ),
        (
            (
                (data.Direction.UP, 1),
                (data.Direction.RIGHT, 1),
                (data.Direction.RIGHT, 1),
            ),
            1,
            (
                (2, 1),
                (1, 1),
            ),
        ),
        (
            ((data.Direction.UP, 1), (data.Direction.RIGHT, 1), (data.Direction.UP, 1)),
            1,
            (
                (1, 2),
                (1, 1),
            ),
        ),
    ),
)
def test_move(
    moves: tuple[tuple[data.Direction, int]],
    tails: int,
    expected: tuple[data.Coordinate],
) -> None:
    head = move.apply(moves, tails)

    i = 0
    current = head
    while current.tail:
        assert current.position == expected[i]
        i += 1
        current = current.tail

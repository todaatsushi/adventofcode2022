import pytest

from src import data, input


@pytest.mark.parametrize(
    "round, expected_register",
    (
        (20, 21),
        (60, 19),
        (100, 18),
        (140, 21),
        (180, 16),
        (220, 18),
    ),
)
def test_program(round: int, expected_register: int) -> None:
    program = input.load("inputs/test.txt")
    program.run()

    assert program.history[round] == expected_register


@pytest.mark.parametrize(
    "round, applying, to_apply",
    (
        (0, data.Command.NOOP, [0]),
        (1, data.Command.ADDX, []),
        (2, data.Command.ADDX, [3]),
        (3, data.Command.ADDX, []),
        (4, data.Command.ADDX, [-5]),
    ),
)
def test_rounds(round: int, applying: data.Command | None, to_apply: list[int]) -> None:
    program = input.load("inputs/dev.txt")
    rounds = program.rounds
    r = rounds[round]

    assert len(rounds) == 5
    assert r.to_apply == to_apply
    assert r.applying == applying

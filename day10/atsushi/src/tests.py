import pytest

from src import input, data


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


def test_rounds() -> None:
    program = input.load("inputs/dev.txt")

    assert len(program.rounds) == 5

    assert program.rounds[0].applying == data.Command.NOOP
    assert program.rounds[1].applying == data.Command.ADDX
    assert program.rounds[2].applying == data.Command.ADDX
    assert program.rounds[3].applying == data.Command.ADDX
    assert program.rounds[4].applying == data.Command.ADDX

import sys

from src import input, models


def solve(file: str, part: int) -> None:
    rounds = input.parse(file, part)
    game = models.Game()
    score = game.play(rounds)

    print(f"Part {part}: total score of {score}")


if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])
    if part not in {1, 2}:
        raise ValueError("Part has to be 1 or 2")

    solve(file, part)

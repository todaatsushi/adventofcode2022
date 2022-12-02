import sys

from src import input, models


def solve(file: str) -> None:
    rounds = input.parse(file)
    game = models.Game()
    score = game.play(rounds)

    print(f"Part 1: total score of {score}")


if __name__ == "__main__":
    file = sys.argv[1]
    solve(file)

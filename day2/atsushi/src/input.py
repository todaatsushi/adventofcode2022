from src import models


def _parse_round(
    line: str, part: int
) -> tuple[models.Throw, models.Throw | models.Result]:
    opp, player = line.split(" ")
    return (
        models.Throw[opp],
        models.Throw[player] if part == 1 else models.Result[player],
    )


def parse(file: str, part: int) -> list[tuple[models.Throw, models.Throw]]:
    rounds = []
    with open(file, "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            round = _parse_round(line, part)
            rounds.append(round)
    return rounds

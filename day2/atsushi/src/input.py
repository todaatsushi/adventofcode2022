from src import models


def _parse_round(line: str) -> tuple[models.Throw, models.Throw]:
    opp, player = line.split(" ")
    return models.Throw[opp], models.Throw[player]


def parse(file: str) -> list[tuple[models.Throw, models.Throw]]:
    rounds = []
    with open(file, "r") as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            round = _parse_round(line)
            rounds.append(round)
    return rounds

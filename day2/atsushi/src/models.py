import enum

ROCK = "ROCK"
SCISSORS = "SCISSORS"
PAPER = "PAPER"


class Throw(enum.Enum):
    A = ROCK
    B = PAPER
    C = SCISSORS

    X = ROCK
    Y = PAPER
    Z = SCISSORS


class Game:
    MATCHUPS: dict[str, str] = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}
    POINTS: dict[str, int] = {
        SCISSORS: 3,
        PAPER: 2,
        ROCK: 1,
    }

    def play(self, rounds: list[tuple[Throw, Throw]]) -> int:
        score = 0

        for opp, player in rounds:
            round_score = 0
            if opp.value == player.value:
                round_score += 3
            elif self.MATCHUPS[player.value] == opp.value:
                round_score += 6

            round_score += self.POINTS[player.value]
            score += round_score
        return score

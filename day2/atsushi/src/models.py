import enum

ROCK = "ROCK"
SCISSORS = "SCISSORS"
PAPER = "PAPER"

WIN = "W"
LOSS = "L"
DRAW = "D"


class Throw(enum.Enum):
    A = ROCK
    B = PAPER
    C = SCISSORS

    X = ROCK
    Y = PAPER
    Z = SCISSORS


class Result(enum.Enum):
    X = LOSS
    Y = DRAW
    Z = WIN


class Game:
    PLAYER_MATCHUPS: dict[str, str] = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}
    RESULT_MATCHUPS: dict[str, dict[str, str]] = {
        WIN: {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK},
        LOSS: PLAYER_MATCHUPS,
        DRAW: {ROCK: ROCK, PAPER: PAPER, SCISSORS: SCISSORS},
    }
    POINTS: dict[str, int] = {
        SCISSORS: 3,
        PAPER: 2,
        ROCK: 1,
    }

    def get_player_input(self, opp: Throw, player_or_result: Throw | Result) -> str:
        if isinstance(player_or_result, Result):
            return self.RESULT_MATCHUPS[player_or_result.value][opp.value]
        return player_or_result.value

    def play(self, rounds: list[tuple[Throw, Throw]]) -> int:
        score = 0
        for opp, player_or_result in rounds:
            player = self.get_player_input(opp, player_or_result)
            round_score = 0
            if opp.value == player:
                round_score += 3
            elif self.PLAYER_MATCHUPS[player] == opp.value:
                round_score += 6

            round_score += self.POINTS[player]
            score += round_score
        return score

from __future__ import annotations

import dataclasses as dc
import enum
import typing as t
from collections import deque

Cycle: t.TypeAlias = int
Cycles: t.TypeAlias = list[Cycle]
CommandLine: t.TypeAlias = tuple["Command", int | None]
Commands: t.TypeAlias = deque[CommandLine]


class Command(enum.Enum):
    NOOP = "noop"
    ADDX = "addx"


EXECUTION_TIMES = {
    Command.NOOP: 1,
    Command.ADDX: 2,
}


@dc.dataclass
class Round:
    to_apply: Cycles
    applying: Command | None = None


@dc.dataclass
class Program:
    rounds: list[Round]
    history: Cycles
    register: int = 1

    @staticmethod
    def build_init_rounds(cmds: Commands) -> list[Round]:
        rounds = []
        for cmd, _ in cmds:
            for _ in range(EXECUTION_TIMES[cmd]):
                rounds.append(Round([]))
        return rounds

    @classmethod
    def new(cls, cmds: Commands) -> Program:
        rounds = cls.build_init_rounds(cmds)
        turn = 0

        while cmds:
            cmd, value = cmds.popleft()
            value = value or 0
            if turn == 180:
                import ipdb

                ipdb.set_trace(context=40)

            while rounds[turn].applying is not None:
                turn += 1

                for _ in range(len(rounds), turn + 2):
                    rounds.append(Round([]))

            rounds[turn].applying = cmd

            if cmd == Command.NOOP:
                rounds[turn].to_apply.append(0)
            else:
                rounds[turn + 1].to_apply.append(value)
                rounds[turn + 1].applying = cmd
            turn += 1
        return cls(rounds=rounds, history=[1])

    def run(self) -> None:
        for round in self.rounds:
            for val in round.to_apply:
                self.register += val
            self.history.append(self.register)

    def get_signal_strength(self, *cycles) -> int:
        tot = 0
        for cycle in cycles:
            tot += cycle * self.history[cycle]
        return tot

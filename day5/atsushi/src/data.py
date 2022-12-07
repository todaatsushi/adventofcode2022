from __future__ import annotations

from collections import deque

import dataclasses


@dataclasses.dataclass
class Move:
    from_stack: int
    to_stack: int
    num: int

    @classmethod
    def new(cls, line: str) -> Move:
        parts = line.strip().split(" ")
        return Move(int(parts[3]) - 1, int(parts[-1]) - 1, int(parts[1]))


class Stack:
    def __init__(self) -> None:
        self.items: list[list[str]] = []

    def __repr__(self) -> str:
        return f"<Stack items={self.items}>"

    @classmethod
    def load_from_input(cls, input: str) -> Stack:
        stack = cls()
        cols, *items = input.split("\n")[::-1]

        for c in cols.split(" "):
            if c:
                stack.items.append([])

        for row in items:
            start, end, col_num = 0, 3, 0
            row = list(row)
            while start < len(row) - 1:
                vals = row[start:end]
                if any(vals) and vals[1].strip():
                    stack.items[col_num].append(vals[1])
                start = end + 1
                end = start + 3
                col_num += 1
        return stack

    def apply(self, move: Move, is_9001: bool = False) -> None:
        while self.items[move.from_stack] and move.num:
            if is_9001:
                to_apply = deque()
                for _ in range(move.num):
                    to_apply.appendleft(self.items[move.from_stack].pop())
                to_apply = list(to_apply)
                move.num = 0
            else:
                to_apply = [self.items[move.from_stack].pop()]
                move.num -= 1

            self.items[move.to_stack].extend(to_apply)

    @property
    def top_crates(self) -> str:
        return "".join([s[-1] for s in self.items])

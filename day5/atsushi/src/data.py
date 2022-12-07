from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class Move:
    from_stack: int
    to_stack: int
    num: int

    @classmethod
    def new(cls, line: str) -> Move:
        parts = line.strip().split(" ")
        return Move(int(parts[3]), int(parts[-1]), int(parts[1]))


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

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

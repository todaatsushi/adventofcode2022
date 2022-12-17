from __future__ import annotations

import enum
from typing import TypeAlias

Moves: TypeAlias = tuple[tuple["Direction", int]]
Coordinate: TypeAlias = tuple[int, int]


class Direction(enum.Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


class Knot:
    position: Coordinate

    def __init__(self, position: Coordinate) -> None:
        self.position = position


class Tail(Knot):
    visited: set[Coordinate]
    tail: "Tail" | None = None

    def __init__(self, position: Coordinate) -> None:
        super().__init__(position)
        self.visited: set[Coordinate] = {position}

    def should_move(self, knot: Knot) -> bool:
        x_diff = abs(self.position[0] - knot.position[0])
        y_diff = abs(self.position[1] - knot.position[1])
        return x_diff > 1 or y_diff > 1

    def adjust(self, knot: Knot, direction: Direction) -> None:
        if not self.should_move(knot):
            return

        modifier = MODIFIERS[direction]
        self.position = (
            knot.position[0] - modifier[0],
            knot.position[1] - modifier[1],
        )
        self.visited.add(self.position)


class Head(Knot):
    tail: Tail

    MODIFIERS = {
        Direction.RIGHT: (1, 0),
        Direction.LEFT: (-1, 0),
        Direction.DOWN: (0, -1),
        Direction.UP: (0, 1),
    }

    def __init__(self, position: Coordinate, num_tails: int) -> None:
        super().__init__(position)

        if num_tails:
            self.tail = Tail(position)
            to_add = num_tails - 1
            current = self.tail

            while to_add:
                current.tail = Tail(position)
                current = current.tail
                to_add -= 1

    def move(self, direction: Direction, distance: int) -> None:
        modifier = self.MODIFIERS[direction]
        while distance > 0:
            self.position = (
                self.position[0] + modifier[0],
                self.position[1] + modifier[1],
            )
            self.tail.adjust(self, direction)
            distance -= 1

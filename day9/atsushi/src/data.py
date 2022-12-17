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

    def get_distance_between(self, knot: Knot) -> tuple[int, int]:
        x_diff = knot.position[0] - self.position[0]
        y_diff = knot.position[1] - self.position[1]
        return x_diff, y_diff

    def should_move(self, knot: Knot) -> bool:
        x, y = self.get_distance_between(knot)
        return abs(x) > 1 or abs(y) > 1

    def get_modified_coords(self, knot: Knot) -> tuple[int, int]:
        x, y = self.get_distance_between(knot)
        if x > 0:
            x = -1
        elif x < 0:
            x = 1

        if y > 0:
            y = -1
        elif y < 0:
            y = 1

        if 0 in {x, y}:
            # If a 1d move, "snap" self to the leading knot
            return (knot.position[0] + x, knot.position[1] + y)
        else:
            # If diagonal, move the knot diagonally
            return (self.position[0] - x, self.position[1] - y)

    def adjust(self, knot: Knot) -> None:
        if not self.should_move(knot):
            return

        coords = self.get_modified_coords(knot)
        self.position = (coords[0], coords[1])
        self.visited.add(self.position)

        if self.tail:
            self.tail.adjust(self)


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
            self.tail.adjust(self)
            distance -= 1

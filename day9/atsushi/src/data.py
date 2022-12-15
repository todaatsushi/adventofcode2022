import enum
from typing import TypeAlias

Moves: TypeAlias = tuple[tuple["Direction", int]]
Coordinate: TypeAlias = tuple[int, int]


class Direction(enum.Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"


MODIFIERS = {
    Direction.RIGHT: (1, 0),
    Direction.LEFT: (-1, 0),
    Direction.DOWN: (0, -1),
    Direction.UP: (0, 1),
}


class Knot:
    position: Coordinate

    def __init__(self, position: Coordinate) -> None:
        self.position = position


class Tail(Knot):
    visited: set[Coordinate]


class Head(Knot):
    tail: Tail

    def __init__(self, position: Coordinate) -> None:
        super().__init__(position)
        self.tail = Tail(position)

    def move(self, direction: Direction, distance: int) -> None:
        modifier = MODIFIERS[direction]

        while distance > 0:
            self.position = (
                self.position[0] + modifier[0],
                self.position[1] + modifier[1],
            )
            distance -= 1

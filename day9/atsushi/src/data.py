import enum
from abc import ABC
from typing import TypeAlias

Moves: TypeAlias = tuple[tuple["Direction", int]]


class Direction(enum.Enum):
    UP = "U"
    RIGHT = "R"
    DOWN = "D"
    LEFT = "L"

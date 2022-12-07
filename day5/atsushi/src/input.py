from __future__ import annotations

from src import data


def load(filepath: str) -> tuple[data.Stack, list[data.Move]]:
    with open(filepath, "r") as f:
        stack, moves = f.read().split("\n\n")

    moves = [data.Move.new(l) for l in moves.split("\n") if l]
    stack = data.Stack.load_from_input(stack)
    return stack, moves

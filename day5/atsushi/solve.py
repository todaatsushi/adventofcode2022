import sys

from src import input


if __name__ == "__main__":
    file = sys.argv[1]
    stack, moves = input.load(file)

    for move in moves:
        stack.apply(move)

    print(f"Part 1: {stack.top_crates}")

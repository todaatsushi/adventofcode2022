import sys

from src import input


if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])
    stack, moves = input.load(file)

    for move in moves:
        stack.apply(move, part == 2)

    print(f"Part {part}: {stack.top_crates}")

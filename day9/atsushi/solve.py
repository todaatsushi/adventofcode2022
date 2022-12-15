import sys

from src import input, move

if __name__ == "__main__":
    part = int(sys.argv[2])
    file = sys.argv[1]

    if part == 1:
        directions = input.load(file)
        head = move.apply(directions)
        tail_visited = len(head.tail.visited)
    else:
        raise NotImplementedError

    print(f"Part {part}: {tail_visited}")

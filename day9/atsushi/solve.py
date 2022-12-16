import sys

from src import input, move

if __name__ == "__main__":
    part = int(sys.argv[2])
    file = sys.argv[1]

    directions = input.load(file)
    if part == 1:
        head = move.apply(directions, 1)
        tail_visited = len(head.tail.visited)
    else:
        head = move.apply(directions, 9)
        t = head.tail
        while t.tail:
            t = t.tail
        tail_visited = len(t.visited)

    print(f"Part {part}: {tail_visited}")

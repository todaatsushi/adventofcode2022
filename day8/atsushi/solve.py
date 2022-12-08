import sys
from src import input

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    if part == 1:
        map = input.load(file)

    print(f"Part {part}: {file}")

import sys

from src import input

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    program = input.load(file)
    program.run()

    total = program.get_signal_strength(20, 60, 100, 140, 180, 220)

    print(f"Part {part}: {total}")

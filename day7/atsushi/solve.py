import sys

from src import input


if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    commands = input.read(file)
    folder = input.load(commands)

    print(f"Part {2}: {file}")

    import ipdb

    ipdb.set_trace(context=40)

import sys

from src import input

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    commands = input.read(file)
    folder = input.load(commands)
    folder.get_size()
    folders = folder.get_folders_with_max_size(100000, set())
    total = sum([x[1] for x in folders])
    print(f"Part {part}: {total}")

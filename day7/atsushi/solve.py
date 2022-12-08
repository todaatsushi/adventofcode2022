import sys

from src import input

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    commands = input.read(file)
    folder = input.load(commands)
    folder.get_size()
    assert folder.size

    if part == 1:
        folders = folder.get_folders_with_size_threshold(100000, set(), False)
        total = sum([x[1] for x in folders])
    else:
        TOTAL_DISK_SIZE = 70000000
        UPDATE_SIZE = 30000000

        unused_space = TOTAL_DISK_SIZE - folder.size
        space_needed = abs(unused_space - UPDATE_SIZE)

        folders = folder.get_folders_with_size_threshold(space_needed, set(), True)
        total = min([f[1] for f in folders])

    print(f"Part {part}: {total}")

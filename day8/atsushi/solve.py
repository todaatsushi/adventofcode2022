import sys

from src import input, search

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    if part == 1:
        map = input.load(file)
        total = search.find_num_visible_trees(map)
    else:
        raise NotImplementedError
    print(f"Part {part}: {total}")

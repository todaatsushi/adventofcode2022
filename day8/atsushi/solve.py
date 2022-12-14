import sys

from src import input, search

if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])

    map = input.load(file)
    if part == 1:
        total = search.find_num_visible_trees(map)
    else:
        total = search.find_scenic_score(map)
    print(f"Part {part}: {total}")

import sys

from src import input


def get_index_of_first_marker(string: str) -> int:
    left, right = 0, 4

    while left < len(string) - 1:
        sub_string = string[left:right]

        if len(set(sub_string)) == 4:
            return right

        left += 1
        right += 1

    raise Exception("Expected a startpoint.")


if __name__ == "__main__":
    file = sys.argv[1]

    for string in input.load(file):
        first_marker_index = get_index_of_first_marker(string)
        print(f"Part 1: {first_marker_index}")

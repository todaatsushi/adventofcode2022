import sys

from src import input


def get_index_of_first_marker(string: str, num_unique_chars: int) -> int:
    left, right = 0, num_unique_chars

    while left < len(string) - 1:
        sub_string = string[left:right]

        if len(set(sub_string)) == num_unique_chars:
            return right

        left += 1
        right += 1

    raise Exception("Expected a startpoint.")


if __name__ == "__main__":
    file = sys.argv[1]
    part = int(sys.argv[2])
    num_unique_chars = {1: 4, 2: 14}[part]

    for string in input.load(file):
        first_marker_index = get_index_of_first_marker(string, num_unique_chars)
        print(f"Part {part}: {first_marker_index}")

import sys

from src import input

if __name__ == "__main__":
    file = sys.argv[1]

    print(input.load(file))

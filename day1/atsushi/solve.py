from sys import argv

from src import data, models


def solve(path: str) -> None:
    total_food_items = data.read_input(path)

    elves = [models.ElfPack.new(food) for food in total_food_items]
    print("Part 1:", models.ElfPack.largest_calorie_total(elves))
    print("Part 2:", models.ElfPack.largest_calorie_total(elves, 3))


if __name__ == "__main__":
    filepath = argv[1]
    solve(filepath)

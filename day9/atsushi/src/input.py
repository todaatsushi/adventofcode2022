from src import data


def load(file: str) -> data.Moves:
    directions: list[tuple[data.Direction, int]] = list()
    with open(file, "r") as f:
        lines = f.readlines()
        for l in lines:
            parts = l.split(" ")
            directions.append((data.Direction(parts[0]), int(parts[1])))
    return tuple(directions)

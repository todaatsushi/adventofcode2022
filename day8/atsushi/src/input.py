def load(file: str) -> list[list[int]]:
    with open(file, "r") as f:
        lines = f.read().splitlines()

    map = []
    for line in lines:
        line = list(line.strip())
        map.append([int(c) for c in line if c])

    return map

from typing import TypeAlias

import numpy as np

Map: TypeAlias = np.ndarray


def load(file: str) -> Map:
    with open(file, "r") as f:
        lines = f.read().splitlines()

    map = []
    for line in lines:
        line = list(line.strip())
        map.append([int(c) for c in line if c])

    return np.array(map)

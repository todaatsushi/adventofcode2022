from typing import Iterable


def load(filepath: str) -> Iterable[str]:
    with open(filepath, "r") as f:
        content = f.read().strip()

    lines = content.split("\n")
    for line in lines:
        if line:
            yield line

def load(filepath: str) -> str:
    with open(filepath, "r") as f:
        content = f.read().strip()
    return content

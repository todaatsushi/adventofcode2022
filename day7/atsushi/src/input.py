from src import data


def read(file: str) -> list[str]:
    with open(file, "r") as f:
        lines = f.readlines()
    return [line for l in lines if (line := l.strip())]


def load(lines: list[str]) -> data.Folder:
    home = data.Folder("/", {}, None)
    current = home

    # Always starts in home
    for line in lines[1:]:
        assert isinstance(current, data.Folder)
        if line.startswith("$ "):
            cmd = line.replace("$ ", "")
            cmd, *args = cmd.split(" ")
            if cmd == "cd":
                if args[0] == "..":
                    current = current.parent
                else:
                    current = current.contents[args[0]]
        else:
            parts = line.split(" ")
            if parts[0].startswith("dir") and isinstance(current, data.Folder):
                content = data.Folder(parts[1], {}, current)
            else:
                content = data.File(parts[1], int(parts[0]))
            name = parts[1]
            current.contents[name] = content
    return home

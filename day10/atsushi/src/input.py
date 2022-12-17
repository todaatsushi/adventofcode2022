from src import data


def load(file: str) -> data.Commands:
    with open(file, "r") as f:
        lines = f.readlines()

    commands: data.Commands = list()

    for line in lines:
        line = line.strip()
        parts = line.split(" ")

        cmd = data.Command(parts[0])

        if cmd == data.Command.NOOP:
            value = None
        else:
            value = int(parts[1])
        commands.append((cmd, value))
    return commands

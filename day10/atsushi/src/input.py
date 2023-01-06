from collections import deque

from src import data


def parse(file: str) -> data.Commands:
    with open(file, "r") as f:
        lines = f.readlines()

    commands: data.Commands = deque()

    for line in lines:
        line = line.strip()
        parts = line.split(" ")

        cmd = data.Command(parts[0])

        if cmd == data.Command.NOOP:
            value = None
        else:
            value = int(parts[1])
        commands.append((cmd, value))
    assert len(commands) == len(lines)
    return commands


def load(file: str) -> data.Program:
    cmds = parse(file)
    return data.Program.new(cmds)

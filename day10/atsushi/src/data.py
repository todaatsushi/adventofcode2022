import enum
import typing as t

Cycle: t.TypeAlias = int
CommandLine: t.TypeAlias = tuple["Command", int | None]
Commands: t.TypeAlias = list[CommandLine]


class Command(enum.Enum):
    NOOP = "noop"
    ADDX = "addx"

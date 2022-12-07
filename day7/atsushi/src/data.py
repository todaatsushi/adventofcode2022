from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class File:
    name: str
    size: int


@dataclasses.dataclass
class Folder:
    name: str
    contents: dict[str, "Folder"]
    parent: "Folder" | None

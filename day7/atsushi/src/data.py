from __future__ import annotations

import dataclasses


@dataclasses.dataclass
class File:
    name: str
    size: int

    def get_size(self) -> int:
        return self.size


@dataclasses.dataclass
class Folder:
    name: str
    contents: dict[str, "Folder" | File]
    parent: "Folder" | None
    size: int | None = None

    def get_size(self) -> int:
        if not self.contents:
            if self.size is None:
                return 0
            return self.size

        total = sum([f.get_size() for f in self.contents.values()])
        self.size = total
        return self.size

    def get_folders_with_max_size(
        self, size: int, folders: set[tuple[str, int]]
    ) -> set[tuple[str, int]]:
        if self.size and self.size <= size:
            folders.add((self.name, self.size))

        for item in self.contents.values():
            if isinstance(item, Folder):
                folders = folders.union(item.get_folders_with_max_size(size, folders))

        return folders

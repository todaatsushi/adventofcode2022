from __future__ import annotations

import dataclasses


def _less_than_or_equal(a, b) -> bool:
    return a <= b


def _more_than_or_equal(a, b) -> bool:
    return a >= b


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

    def get_folders_with_size_threshold(
        self, size: int, folders: set[tuple[str, int]], need_above_size: bool
    ) -> set[tuple[str, int]]:
        f = _more_than_or_equal if need_above_size else _less_than_or_equal
        if self.size and f(self.size, size):
            folders.add((self.name, self.size))

        for item in self.contents.values():
            if isinstance(item, Folder):
                folders = folders.union(
                    item.get_folders_with_size_threshold(size, folders, need_above_size)
                )

        return folders

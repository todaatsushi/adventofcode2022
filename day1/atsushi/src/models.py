from __future__ import annotations

import dataclasses as dc


@dc.dataclass
class ElfPack:
    calories: list[int]
    total: int

    @classmethod
    def new(cls, calories: list[int]) -> ElfPack:
        return cls(calories=calories, total=sum(calories))

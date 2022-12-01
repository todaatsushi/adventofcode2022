from __future__ import annotations

import dataclasses as dc


@dc.dataclass
class ElfPack:
    calories: list[int]
    total: int

    @classmethod
    def new(cls, calories: list[int]) -> ElfPack:
        return cls(calories=calories, total=sum(calories))

    @staticmethod
    def largest_calorie_total(elves: list[ElfPack]) -> int:
        return max([elf.total for elf in elves])

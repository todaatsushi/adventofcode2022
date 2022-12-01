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
    def largest_calorie_total(elves: list[ElfPack], num_elves: int = 1) -> int:
        by_total_calories = [
            elf.total for elf in sorted(elves, key=lambda elf: elf.total, reverse=True)
        ]
        return sum(by_total_calories[:num_elves])

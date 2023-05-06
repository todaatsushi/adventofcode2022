use std::ops::RangeInclusive;

use crate::inputs;

pub fn solve() {
    let pairs = inputs::read();
    let mut count = 0;

    pairs.lines().for_each(|pair| {
        let parts: Vec<u16> = pair
            .split([',', '-'].as_ref())
            .collect::<Vec<&str>>()
            .into_iter()
            .map(|v| v.parse().unwrap())
            .collect();

        let elf_1_range = RangeInclusive::new(parts[0], parts[1]);
        let elf_2_range = RangeInclusive::new(parts[2], parts[3]);
        let elf_1_in_elf_2 = elf_2_range.contains(&parts[0]) || elf_2_range.contains(&parts[1]);
        let elf_2_in_elf_1 = elf_1_range.contains(&parts[2]) || elf_1_range.contains(&parts[3]);

        if elf_1_in_elf_2 || elf_2_in_elf_1 {
            count += 1;
        }
    });

    println!("Total partially overlapping pairs: {}", count);
}

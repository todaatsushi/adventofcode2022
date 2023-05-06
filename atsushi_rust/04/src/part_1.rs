use crate::inputs;

fn get_zones(elf_zones: &str) -> [u16; 2] {
    let mut res: [u16; 2] = [0, 0];
    let vals = elf_zones
        .split_once("-")
        .expect("Zones not separated by '-'");

    res[0] = vals.0.parse().unwrap();
    res[1] = vals.1.parse().unwrap();
    res
}

pub fn solve() {
    let pairs = inputs::read();

    let mut count: u16 = 0;

    pairs.lines().into_iter().for_each(|pair| {
        let (elf_1, elf_2) = pair
            .split_once(",")
            .expect("Bad line: couldn't discern pair zones.");

        let elf_1_zones = get_zones(elf_1);
        let elf_2_zones = get_zones(elf_2);

        let mut all_zones: [u16; 4] = [
            elf_2_zones[0],
            elf_2_zones[1],
            elf_1_zones[0],
            elf_1_zones[1],
        ];

        all_zones.sort();
        let min = all_zones[0];
        let max = all_zones[3];

        let elf_zones_1_match = min == elf_1_zones[0] && max == elf_1_zones[1];
        let elf_zones_2_match = min == elf_2_zones[0] && max == elf_2_zones[1];

        if elf_zones_1_match || elf_zones_2_match {
            count += 1;
        }
    });

    println!("Total overlapping pairs: {}", count);
}

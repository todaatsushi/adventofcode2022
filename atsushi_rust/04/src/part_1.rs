use crate::inputs;

pub fn solve() {
    let pairs = inputs::read();

    let mut count: u16 = 0;

    pairs.lines().into_iter().for_each(|pair| {
        let mut parts: Vec<u16> = pair
            .split([',', '-'].as_ref())
            .collect::<Vec<&str>>()
            .into_iter()
            .map(|v| v.parse().unwrap())
            .collect();

        let elf_1: [u16; 2] = [parts[0], parts[1]];
        let elf_2: [u16; 2] = [parts[2], parts[3]];
        parts.sort();

        let match_1 = parts[0] == elf_1[0] && parts[3] == elf_1[1];
        let match_2 = parts[0] == elf_2[0] && parts[3] == elf_2[1];

        if match_1 || match_2 {
            count += 1;
        }
    });

    println!("Total completely overlapping pairs: {}", count);
}

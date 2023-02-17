use day_1::load_data;

fn main() {
    let mut elves = load_data();
    let max_calories_elf = elves.iter().max_by_key(|elf| elf.total_calories).unwrap();
    println!("Part 1: {:?}", max_calories_elf);

    elves.sort_by_key(|elf| elf.total_calories);
    let num_elves = elves.len();
    let top_3: Vec<u32> = elves[num_elves - 3..]
        .iter()
        .map(|elf| elf.total_calories)
        .collect();
    let total: u32 = top_3.iter().sum();

    println!("Part 2: {:?}", total);
}

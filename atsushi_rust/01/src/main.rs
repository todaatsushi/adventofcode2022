use day_1::load_data;

fn main() {
    let elves = load_data();
    let max_calories_elf = elves.iter().max_by_key(|elf| elf.total_calories).unwrap();
    println!("Part 1: {:?}", max_calories_elf);
}

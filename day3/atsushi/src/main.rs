use atsushi::input::read_file;

fn main() {
    let rucksacks = read_file();
    let priority_sum: Option<u32> = rucksacks
        .into_iter()
        .map(|r| r.get_missing_item_score())
        .reduce(|tot, sum| tot + sum);

    match priority_sum {
        Some(v) => println!("Part1 total of priority items: {}", v),
        None => panic!("No total"),
    }
}

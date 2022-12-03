use atsushi::data::get_common_items_in_rucksack_intervals;
use std::env;

use atsushi::input::read_file;

fn main() {
    let part: Vec<String> = env::args().collect();
    let rucksacks = read_file();

    match part[3].parse().unwrap() {
        1 => {
            let priority_sum: Option<u32> = rucksacks
                .into_iter()
                .map(|r| r.get_missing_item_score())
                .reduce(|tot, sum| tot + sum);

            match priority_sum {
                Some(v) => println!("Part1 total of priority items: {}", v),
                None => panic!("No total"),
            }
        }
        2 => {
            let total = get_common_items_in_rucksack_intervals(rucksacks, 3);
            println!("Part2 total of common items: {}", total)
        }
        _ => panic!("Has to be 1 or 2"),
    }
}

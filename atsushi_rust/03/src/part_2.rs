use std::collections::HashSet;

use crate::{input, score};

fn get_repeated_items_in_bags(first: &str, second: &str, third: &str) -> char {
    let first_chars: HashSet<char> = first.chars().collect();
    let common_in_first_and_second: HashSet<char> =
        second.chars().filter(|c| first_chars.contains(c)).collect();

    third
        .chars()
        .filter(|c| common_in_first_and_second.contains(c))
        .collect::<Vec<char>>()[0]
}

pub fn solve() -> u16 {
    let content = input::read();
    let lines: Vec<_> = content.lines().collect();
    let num_lines = lines.len();
    let mut chars: Vec<char> = vec![];

    for i in (0..num_lines).step_by(3) {
        let first = lines[i];
        let second = lines[i + 1];
        let third = lines[i + 2];

        let c = get_repeated_items_in_bags(first, second, third);
        chars.push(c);
    }
    chars.into_iter().map(|c| score::get(c)).sum()
}

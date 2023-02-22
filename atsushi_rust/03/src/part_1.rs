use crate::{input, score};

use std::collections::HashSet;

fn get_repeated_items_in_bag(bag: String) -> char {
    let index = bag.chars().count() / 2;
    let first = bag[..index].to_string();
    let second = bag[index..].to_string();

    let chars: HashSet<char> = first.chars().collect();
    second
        .chars()
        .filter(|c| chars.contains(c))
        .collect::<Vec<char>>()[0]
}

fn get_repeated_items_in_bags(bags: String) -> Vec<char> {
    bags.lines()
        .into_iter()
        .map(|l| get_repeated_items_in_bag(l.to_string()))
        .collect()
}

pub fn solve() -> u16 {
    let content = input::read();
    let common = get_repeated_items_in_bags(content);
    common.iter().map(|&c| score::get(c)).sum()
}

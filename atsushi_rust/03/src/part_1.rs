use crate::input;

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

fn get_score(c: char) -> u16 {
    static ASCII_LOWER: [char; 26] = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    ];
    let modifier: u16;
    if c.is_lowercase() {
        modifier = 1;
    } else {
        modifier = 27;
    }
    let c_lower: Vec<char> = c.to_lowercase().collect();
    let val = ASCII_LOWER
        .iter()
        .position(|&check| check == c_lower[0])
        .unwrap();
    val as u16 + modifier
}

pub fn solve() -> u16 {
    let content = input::read();
    let common = get_repeated_items_in_bags(content);
    common.iter().map(|&c| get_score(c)).sum()
}

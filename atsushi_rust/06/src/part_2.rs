use std::collections::HashSet;

use crate::inputs;

fn get_index_of_unique_chars(s: &str) -> u16 {
    let mut left: usize = 0;
    let mut right: usize = 14;
    let chars: Vec<char> = s.chars().collect();

    while left < right && right < s.len() {
        let mut unique: HashSet<char> = HashSet::new();

        for idx in left..right {
            unique.insert(chars[idx]);
        }

        if unique.len() == 14 {
            break;
        }

        left += 1;
        right += 1;
    }

    return right as u16;
}

pub fn solve() {
    let raw_input = inputs::read();

    raw_input.lines().for_each(|line| {
        println!("{}: {}", line, get_index_of_unique_chars(line));
    });
}

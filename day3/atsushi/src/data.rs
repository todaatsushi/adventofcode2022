use std::{collections::HashSet, result::Result, str::FromStr, string::ParseError};

pub fn get_score(c: char) -> u32 {
    let index = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        .find(c)
        .unwrap() as u32;

    index + 1
}

#[derive(Debug)]
pub struct Rucksack {
    items: String,
}

#[derive(Debug)]
enum RucksackErr {
    NoCommonItem,
}

impl FromStr for Rucksack {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        Ok(Rucksack {
            items: s.to_string(),
        })
    }
}

impl Rucksack {
    fn split_items_into_compartments(&self) -> [String; 2] {
        let s = &self.items;
        let index = s.chars().count() / 2;
        let first = s[..index].to_string();
        let second = s[index..].to_string();

        [first, second]
    }

    fn find_common_item_in_rucksack_compartments(&self) -> Result<char, RucksackErr> {
        let compartments = self.split_items_into_compartments();
        let first = compartments[0].chars();
        let second = &compartments[1];

        for c in first {
            if second.contains(c) {
                return Ok(c);
            }
        }
        Err(RucksackErr::NoCommonItem)
    }

    pub fn get_missing_item_score(self: &Self) -> u32 {
        let common_item = self.find_common_item_in_rucksack_compartments().unwrap();
        get_score(common_item)
    }
}

fn get_common_items_for_rucksacks(rucksacks: &[Rucksack]) -> char {
    let mut sets: Vec<HashSet<char>> = Vec::new();
    for r in rucksacks {
        let r_items_set: HashSet<char> = r.items.chars().collect();
        sets.extend(vec![r_items_set]);
    }

    let intersection = sets[0]
        .intersection(&sets[1])
        .find(|e| sets[2].contains(e))
        .unwrap();
    intersection.clone()
}

pub fn get_common_items_in_rucksack_intervals(rucksacks: Vec<Rucksack>, interval: usize) -> u32 {
    let rucksack_items: Vec<&String> = rucksacks.iter().map(|r| &r.items).collect();
    let mut common_items_scores: Vec<u32> = Vec::new();

    let mut left = 0 as usize;
    let mut right = interval as usize;

    while right <= rucksack_items.len() {
        let common = get_common_items_for_rucksacks(&rucksacks[left..right]);
        common_items_scores.push(get_score(common));
        left += interval;
        right += interval;
    }

    let mut tot = 0;
    for score in common_items_scores {
        tot += score;
    }
    tot
}

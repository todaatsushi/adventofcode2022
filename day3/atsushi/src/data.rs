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

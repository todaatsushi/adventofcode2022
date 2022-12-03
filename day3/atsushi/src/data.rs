use std::{result::Result, str::FromStr, string::ParseError};

#[derive(Debug)]
pub struct Rucksack {
    compartments: [String; 2],
}

#[derive(Debug)]
enum RucksackErr {
    NoCommonItem,
}

impl FromStr for Rucksack {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let index = s.chars().count() / 2;
        let first = s[..index].to_string();
        let second = s[index..].to_string();

        Ok(Rucksack {
            compartments: [first, second],
        })
    }
}

impl Rucksack {
    fn get_score(&self, c: char) -> u32 {
        let index = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            .find(c)
            .unwrap() as u32;

        index + 1
    }

    fn find_common_item(&self) -> Result<char, RucksackErr> {
        let first = self.compartments[0].chars();
        let second = &self.compartments[1];

        for c in first {
            if second.contains(c) {
                return Ok(c);
            }
        }
        Err(RucksackErr::NoCommonItem)
    }

    pub fn get_missing_item_score(self: &Self) -> u32 {
        let common_item = self.find_common_item().unwrap();
        self.get_score(common_item)
    }
}

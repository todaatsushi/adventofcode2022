use std::str::FromStr;
use std::string::ParseError;

#[derive(Debug)]
pub struct Rucksack {
    compartments: [String; 2],
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

use std::{env, fs};

use std::str::FromStr;
use std::string::ParseError;

#[derive(Debug)]
enum InputError {
    InvalidArgs,
    BadNumOfArgs,
}

fn get_file() -> Result<&'static str, InputError> {
    let args: Vec<String> = env::args().collect();

    match args.len() as i32 {
        2 => {
            let file = match args[1].as_str() {
                "test" => Some("./inputs/test.txt"),
                "puzzle" => Some("./inputs/puzzle.txt"),
                _ => None,
            };
            match file {
                Some(f) => Ok(f),
                None => Err(InputError::InvalidArgs),
            }
        }
        _ => Err(InputError::BadNumOfArgs),
    }
}

#[derive(Debug)]
pub struct Elf {
    pub total_calories: u32,
}

impl FromStr for Elf {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let total: u32 = s
            .split("\n")
            .map(|v| v.parse::<u32>().unwrap())
            .reduce(|a, v| a + v)
            .unwrap();

        Ok(Self {
            total_calories: total,
        })
    }
}

pub fn load_data() -> Vec<Elf> {
    let file = get_file().unwrap().to_string();
    let content = fs::read_to_string(file).expect("Couldn't read file");

    let elves: Vec<Elf> = content
        .trim()
        .split("\n\n")
        .map(str::parse)
        .map(Result::unwrap)
        .collect();
    elves
}

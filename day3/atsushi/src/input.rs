use crate::data::Rucksack;
use std::{env, str::Lines};

#[derive(Debug)]
enum InputError {
    FileDoesntExist,
    Need3Args,
}

fn read_input() -> Lines<'static> {
    let args: Vec<String> = env::args().collect();
    let lines = match args.len() as u8 {
        3 => match args[2].as_str() {
            "test" => Ok(include_str!("../inputs/test.txt")),
            "puzzle" => Ok(include_str!("../inputs/puzzle.txt")),
            _ => Err(InputError::FileDoesntExist),
        },
        _ => Err(InputError::Need3Args),
    }
    .unwrap()
    .lines();

    lines
}

pub fn read_file() -> Vec<Rucksack> {
    let input = read_input();
    let rucksacks: Vec<Rucksack> = input.map(str::parse).map(Result::unwrap).collect();

    rucksacks
}

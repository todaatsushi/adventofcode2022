use std::{collections::LinkedList, env, fs};

use crate::data::{create_stacks, Instruction};

#[derive(Debug)]
enum InputError {
    InvalidArgs,
    BadNumberOfArgs,
}

const TEST_INPUT_PATH: &str = "./inputs/test.txt";
const PUZZLE_INPUT_PATH: &str = "./inputs/puzzle.txt";

fn get_file() -> Result<&'static str, InputError> {
    let args: Vec<String> = env::args().collect();

    match args.len() as u8 {
        2 => match args[1].as_str() {
            "test" => Ok(TEST_INPUT_PATH),
            "puzzle" => Ok(PUZZLE_INPUT_PATH),
            _ => Err(InputError::InvalidArgs),
        },
        _ => Err(InputError::BadNumberOfArgs),
    }
}

pub fn read() -> (Vec<LinkedList<char>>, Vec<Instruction>) {
    let filename = get_file().expect("Couldn't fetch the correct file to use.");
    let content = fs::read_to_string(filename).expect("Couldn't read the file");

    let parts = content.split_once("\n\n").unwrap();
    let instructions = parts
        .1
        .trim()
        .split("\n")
        .into_iter()
        .map(str::parse)
        .map(Result::unwrap)
        .collect::<Vec<Instruction>>();

    let supply_stacks = create_stacks(parts.0);
    return (supply_stacks, instructions);
}

use std::{env, fs, str};

#[derive(Debug)]
pub enum InputError {
    InvalidArgs,
    BadNumOfArgs,
}

const TEST_INPUT_PATH: &str = "./inputs/test.txt";
const PUZZLE_INPUT_PATH: &str = "./inputs/puzzle.txt";

fn get_file() -> Result<&'static str, InputError> {
    let args: Vec<String> = env::args().collect();

    match args.len() as u8 {
        2 => {
            let file = match args[1].as_str() {
                "test" => Some(TEST_INPUT_PATH),
                "puzzle" => Some(PUZZLE_INPUT_PATH),
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

pub fn read() -> String {
    let file = get_file().expect("Couldn't fetch the correct file to use");
    fs::read_to_string(file).expect("Couldn't read the file.")
}

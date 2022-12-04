use std::{env, str::Lines};

#[derive(Debug)]
enum InputError {
    FileDoesntExist,
    Need4Args,
}

pub fn read_input() -> Lines<'static> {
    let args: Vec<String> = env::args().collect();
    let lines = match args.len() as u8 {
        4 => match args[2].as_str() {
            "test" => Ok(include_str!("../inputs/test.txt")),
            "puzzle" => Ok(include_str!("../inputs/puzzle.txt")),
            _ => Err(InputError::FileDoesntExist),
        },
        _ => Err(InputError::Need4Args),
    }
    .unwrap()
    .lines();

    lines
}

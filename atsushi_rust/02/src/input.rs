use std::env;

#[derive(Debug)]
pub enum InputError {
    InvalidArgs,
    BadNumOfArgs,
}

pub fn get_file() -> Result<&'static str, InputError> {
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

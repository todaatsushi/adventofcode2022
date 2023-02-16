use std::{env, fs};

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

pub fn load_data() {
    let file = get_file().unwrap().to_string();
    let file_contents = fs::read_to_string(file).expect("Couldn't read file");
    todo!()
}

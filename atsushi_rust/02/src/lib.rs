use std::{env, fs};

use std::str::FromStr;

#[derive(Debug, PartialEq)]
enum Choice {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl FromStr for Choice {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(Choice::Rock),
            "A" => Ok(Choice::Rock),
            "Y" => Ok(Choice::Paper),
            "B" => Ok(Choice::Paper),
            "Z" => Ok(Choice::Scissors),
            "C" => Ok(Choice::Scissors),
            _ => Err(()),
        }
    }
}
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

fn get_round_points(p: &str, e: &str) -> u32 {
    let player = Choice::from_str(p).expect("Couldn't match enum for player");
    let elf = Choice::from_str(e).expect("Couldn't match enum for elf");
    let mut total: u32 = 0;

    if player == elf {
        total += 3;
    } else if (player == Choice::Rock && elf == Choice::Scissors)
        || (player == Choice::Paper && elf == Choice::Rock)
        || (player == Choice::Scissors && elf == Choice::Paper)
    {
        total += 6;
    }
    println!("Player: {:?}, Elf: {:?}", &player, &elf);
    total += player as u32;
    println!("Total: {}\n", &total);
    total
}

pub fn part_1() -> u32 {
    let file = get_file().unwrap().to_string();
    let content = fs::read_to_string(file).expect("Couldn't read file");

    let rounds: u32 = content
        .trim()
        .split("\n")
        .into_iter()
        .map(|line| line.split_once(" ").unwrap())
        .map(|(p, e)| get_round_points(e, p))
        .sum();
    rounds
}

#[cfg(test)]
mod tests {
    use super::get_round_points;

    #[test]
    fn test_player_rock() {
        let expected_totals: [u32; 3] = [4, 1, 7];
        for (i, e) in ["A", "B", "C"].iter().enumerate() {
            let total = get_round_points("X", e);
            assert_eq!(total, expected_totals[i]);
        }
    }

    #[test]
    fn test_player_paper() {
        let expected_totals: [u32; 3] = [8, 5, 2];
        for (i, e) in ["A", "B", "C"].iter().enumerate() {
            let total = get_round_points("Y", e);
            assert_eq!(total, expected_totals[i]);
        }
    }

    #[test]
    fn test_player_scissors() {
        let expected_totals: [u32; 3] = [3, 9, 6];
        for (i, e) in ["A", "B", "C"].iter().enumerate() {
            let total = get_round_points("Z", e);
            assert_eq!(total, expected_totals[i]);
        }
    }
}

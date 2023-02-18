use std::fs;

use crate::input::get_file;
use std::str::FromStr;

#[derive(Debug, PartialEq)]
enum RoundResult {
    Win = 6,
    Draw = 3,
    Loss = 0,
}

impl FromStr for RoundResult {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(RoundResult::Loss),
            "Y" => Ok(RoundResult::Draw),
            "Z" => Ok(RoundResult::Win),
            _ => Err(()),
        }
    }
}

#[derive(Debug, PartialEq, Clone)]
enum Choice {
    Rock = 1,
    Paper = 2,
    Scissors = 3,
}

impl FromStr for Choice {
    type Err = ();

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "A" => Ok(Choice::Rock),
            "B" => Ok(Choice::Paper),
            "C" => Ok(Choice::Scissors),
            _ => Err(()),
        }
    }
}

impl Choice {
    pub fn from_elf_and_result(e: Choice, r: &RoundResult) -> Choice {
        match r {
            RoundResult::Draw => e.clone(),
            RoundResult::Win => match e {
                Choice::Scissors => Choice::Rock,
                Choice::Rock => Choice::Paper,
                Choice::Paper => Choice::Scissors,
            },
            RoundResult::Loss => match e {
                Choice::Scissors => Choice::Paper,
                Choice::Rock => Choice::Scissors,
                Choice::Paper => Choice::Rock,
            },
        }
    }
}

fn get_round_points(e: &str, r: &str) -> u32 {
    let elf = Choice::from_str(e).expect("Couldn't match enum for player");
    let res = RoundResult::from_str(r).expect("Couldn't match enum for result");
    let player = Choice::from_elf_and_result(elf, &res);
    let total: u32 = player as u32 + res as u32;
    total
}

pub fn part_2() -> u32 {
    let file = get_file().unwrap().to_string();
    let content = fs::read_to_string(file).expect("Couldn't read file");

    let x: u32 = content
        .trim()
        .split("\n")
        .into_iter()
        .map(|line| line.split_once(" ").unwrap())
        .map(|(e, r)| get_round_points(e, r))
        .sum();

    println!("{}", &x);
    x
}

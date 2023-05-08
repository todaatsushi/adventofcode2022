use std::{collections::LinkedList, str::FromStr, string::ParseError};

#[derive(Debug)]
pub struct Instruction {
    pub n: u16,
    pub from: usize,
    pub to: usize,
}

impl FromStr for Instruction {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let parts: Vec<_> = s.split(" ").collect();

        Ok(Self {
            n: parts[1].parse().expect("Couldn't parse the move amount"),
            from: parts[3]
                .parse::<usize>()
                .expect("Couldn't parse from value")
                - 1,
            to: parts[5].parse::<usize>().expect("Couldn't parse to value") - 1,
        })
    }
}

pub fn create_stacks(input: &str) -> Vec<LinkedList<char>> {
    let mut stacks: Vec<LinkedList<char>> = vec![];
    input
        .split("\n")
        .into_iter()
        .map(str::as_bytes)
        .for_each(|line| {
            for c in (0..line.len()).step_by(4) {
                let idx = c + 1;
                let val = line[idx] as char;
                let stack_num = (c + 1) / 4;

                if stacks.len() < stack_num + 1 {
                    stacks.push(LinkedList::from([]));
                }

                if line[idx] != 32 {
                    stacks[stack_num].push_back(val);
                }
            }
        });

    return stacks;
}

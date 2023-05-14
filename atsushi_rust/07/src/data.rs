use std::collections::HashMap;
use std::str::FromStr;
use std::string::ParseError;

#[derive(Debug)]
pub enum Type {
    Directory,
    File,
}

#[derive(Debug)]
pub struct SysObj<'a> {
    pub name: &'a str,
    pub obj_type: Type,
    pub size: u16,
    pub children: Box<HashMap<&'a str, &'a SysObj<'a>>>,
    pub parent: Box<Option<&'a SysObj<'a>>>,
}

#[derive(Debug)]
pub enum Command {
    CD(String),
    LS,
}

impl FromStr for Command {
    type Err = ParseError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let elems: Vec<&str> = s.split(" ").collect();
        let cmd = elems[1];

        match cmd {
            "cd" => Ok(Command::CD(elems[2].to_owned())),
            "ls" => Ok(Command::LS),
            _ => panic!("TODO: figure this out"),
        }
    }
}

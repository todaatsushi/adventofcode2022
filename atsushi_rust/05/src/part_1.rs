use std::collections::LinkedList;

use crate::inputs::read;

pub fn solve() -> LinkedList<char> {
    let mut result: LinkedList<char> = LinkedList::new();
    let (mut stacks, instructions) = read();

    instructions.into_iter().for_each(|instruction| {
        let mut items_to_move = vec![];
        for _ in 0..instruction.n {
            let c = stacks[instruction.from].pop_back().unwrap();
            items_to_move.push(c);
        }

        for i in items_to_move {
            stacks[instruction.to].push_back(i);
        }
    });

    for mut s in stacks {
        result.push_back(s.pop_back().unwrap());
    }
    return result;
}

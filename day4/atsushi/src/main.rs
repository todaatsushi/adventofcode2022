use atsushi::data::read_input;
use std::env;

fn get_section_vec(pair: Vec<&str>, arr_len: i8, offset: i8) -> [Vec<i8>; 2] {
    let vals = pair
        .iter()
        .map(|p| {
            p.split("-")
                .map(|n| n.parse::<i8>().unwrap())
                .collect::<Vec<i8>>()
        })
        .map(|p| {
            let mut sec: Vec<i8> = vec![0; arr_len as usize];

            for mut i in p[0]..p[1] + 1 {
                i -= offset;
                sec[i as usize] += 1;
            }
            sec
        })
        .collect::<Vec<_>>();

    if vals[0].iter().sum::<i8>() > vals[1].iter().sum::<i8>() {
        [vals[0].clone(), vals[1].clone()]
    } else {
        [vals[1].clone(), vals[0].clone()]
    }
}

fn parse_file() -> Vec<[Vec<i8>; 2]> {
    let raw_pairs = read_input()
        .into_iter()
        .map(|l| l.split(",").into_iter().collect::<Vec<&str>>())
        .map(|pair| {
            let vals = pair
                .iter()
                .map(|p| {
                    p.split("-")
                        .map(|n| n.parse::<i8>().unwrap())
                        .collect::<Vec<i8>>()
                })
                .collect::<Vec<_>>();
            let min = &vals.iter().flatten().min().unwrap();
            let max = &vals.iter().flatten().max().unwrap();
            let arr_len = (**min - **max).abs() + 1;

            get_section_vec(pair, arr_len, **min)
        });
    raw_pairs.collect::<Vec<[Vec<i8>; 2]>>()
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let part = args[3].parse::<u8>().unwrap();
    let mut non_overlapping_pairs = 0;

    let section_pairs = parse_file();

    for sp in &section_pairs {
        let arr_len = &sp[0].len();

        for i in 0..*arr_len {
            let condition = match &part {
                1 => sp[1][i] == 1 && sp[0][i] != 1,
                2 => sp[0][i] == 1 && sp[1][i] == 1,
                _ => panic!("Part has to be 1 or 2"),
            };

            if condition {
                non_overlapping_pairs += 1;
                break;
            }
        }
    }

    let answer = match &part {
        1 => section_pairs.len() - non_overlapping_pairs,
        2 => non_overlapping_pairs,
        _ => panic!("Part has to be 1 or 2"),
    };

    println!("Part {}: number of pairs - {}", part, answer);
}

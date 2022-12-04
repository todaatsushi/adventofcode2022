use atsushi::data::read_input;

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
    let mut non_overlapping_pairs = 0;

    let section_pairs = parse_file();

    for sp in &section_pairs {
        let arr_len = &sp[0].len();

        for i in 0..*arr_len {
            if sp[1][i] == 1 && sp[0][i] != 1 {
                non_overlapping_pairs += 1;
                break;
            }
        }
    }

    println!(
        "Part 1: number of pairs with total overlap - {}",
        section_pairs.len() - non_overlapping_pairs
    );
}

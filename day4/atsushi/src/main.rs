use atsushi::data::read_input;

fn get_section_vec(pair: Vec<&str>) -> [[u8; 9]; 2] {
    let vals = pair
        .iter()
        .map(|p| {
            p.split("-")
                .map(|n| n.parse::<u8>().unwrap())
                .collect::<Vec<u8>>()
        })
        .map(|p| {
            let mut sec: [u8; 9] = [0; 9];

            for mut i in p[0]..p[1] + 1 {
                i -= 1;
                sec[i as usize] += 1;
            }
            sec
        })
        .collect::<Vec<_>>();

    if vals[0].iter().sum::<u8>() > vals[1].iter().sum::<u8>() {
        [vals[0], vals[1]]
    } else {
        [vals[1], vals[0]]
    }
}

fn parse_file() -> Vec<[[u8; 9]; 2]> {
    let raw_pairs = read_input()
        .into_iter()
        .map(|l| l.split(",").into_iter().collect::<Vec<&str>>())
        .map(|p| get_section_vec(p));
    raw_pairs.collect::<Vec<[[u8; 9]; 2]>>()
}

fn main() {
    let mut non_overlapping_pairs = 0;

    let section_pairs = parse_file();

    for sp in &section_pairs {
        for i in 0..9 {
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

use atsushi::data::read_input;

fn get_section_vec(pair: Vec<&str>) -> [Vec<u8>; 2] {
    let vals = pair
        .iter()
        .map(|p| {
            p.split("-")
                .map(|n| n.parse::<u8>().unwrap())
                .collect::<Vec<u8>>()
        })
        .map(|p| {
            let mut sec: Vec<u8> = vec![0; 9];

            for mut i in p[0]..p[1] + 1 {
                i -= 1;
                sec[i as usize] += 1;
            }
            sec
        })
        .collect::<Vec<_>>();

    if vals[0].iter().sum::<u8>() > vals[1].iter().sum::<u8>() {
        [vals[0].clone(), vals[1].clone()]
    } else {
        [vals[1].clone(), vals[0].clone()]
    }
}

fn parse_file() -> Vec<[Vec<u8>; 2]> {
    let raw_pairs = read_input()
        .into_iter()
        .map(|l| l.split(",").into_iter().collect::<Vec<&str>>())
        .map(|p| get_section_vec(p));
    raw_pairs.collect::<Vec<[Vec<u8>; 2]>>()
}

fn main() {
    let section_pairs = parse_file();

    for sp in section_pairs {
        println!("{:?}", sp);
    }
}

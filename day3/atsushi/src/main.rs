use atsushi::input::read_file;

fn main() {
    let rucksacks = read_file();

    for r in rucksacks {
        println!("{:?}", r);
    }
}

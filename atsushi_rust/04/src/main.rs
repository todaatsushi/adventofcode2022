use day_4::inputs;

fn main() {
    let f = inputs::read();

    f.lines().into_iter().for_each(|l| println!("{:?}", l));
}

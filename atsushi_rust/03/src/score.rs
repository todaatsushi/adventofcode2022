static ASCII_LOWER: [char; 26] = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z',
];

pub fn get(c: char) -> u16 {
    let modifier: u16;
    if c.is_lowercase() {
        modifier = 1;
    } else {
        modifier = 27;
    }
    let c_lower: Vec<char> = c.to_lowercase().collect();
    let val = ASCII_LOWER
        .iter()
        .position(|&check| check == c_lower[0])
        .unwrap();
    val as u16 + modifier
}

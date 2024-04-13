use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let line = lines
        .next()
        .unwrap()
        .unwrap();

    let mut split = line
        .split(" ");

    let y = split.next().unwrap();
    let p = split.next().unwrap();

    let yv = y
        .chars()
        .collect::<Vec<_>>();

    let n = yv.len();

    let v = vec!['a', 'e', 'i', 'o', 'u'];

    let ny = match (yv[n - 2], yv[n - 1]) {
        ('e', 'x')                => {
            yv
                .iter()
                .map(|&c| c)
                .collect::<String>()
    },
        (_, c) if v.contains(&c)  => {
            yv
                .iter()
                .map(|&c| c)
                .take(n - 1)
                .chain("ex".chars())
                .collect::<String>()
        },
        rest                     => {
            yv
                .iter()
                .map(|&c| c)
                .chain("ex".chars())
                .collect::<String>()
        },
    };

    println!("{}{}", ny, p);

    Ok(())
}

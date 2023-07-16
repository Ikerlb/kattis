use std::io::{self, BufRead};

fn pow(n: usize, k: usize, m: usize) -> usize {
    if k == 0 {
        return 1;
    } else if k % 2 == 0 {
        let half = pow(n, k >> 1, m);
        return (half * half) % m;
    } else {
        let half = pow(n, k >> 1, m);
        return (((half * half) % m) * n) % m;
    }
}

fn main() -> io::Result<()> {
    let mut lines = io::stdin()
        .lock()
        .lines();
    let first = lines
        .next()
        .unwrap()?;
    let mut split = first
        .split(" ")
        .map(|x| x.parse::<usize>().unwrap());
    let a = split.next().unwrap();
    let b = split.next().unwrap();

    let s = (1..=a)
        .map(|k| pow(k, b, a))
        .sum::<usize>() % a;

    println!("{}", s);

    return Ok(());
}

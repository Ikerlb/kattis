use std::io::{BufRead, self};

fn divisors(n: usize) -> Vec<(usize, usize)> {
    let mut res = Vec::new();
    for i in 1..=n {
        if n % i == 0 {
            res.push((i, n / i));
        }
    }
    return res;
}

fn solve(line: &str) -> usize {
    let chars = line.chars().collect::<Vec<_>>();
    for (d1, d2) in divisors(line.len()) {
        let mult = chars[..d1 as usize]
            .iter()
            .collect::<String>()
            .repeat(d2);
        if &mult == line {
            return d2;
        }
    }
    return 0;
}

fn main() -> io::Result<()> {
    let mut lines = io::stdin()
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;

    lines.pop(); // pop "." 

    for line in &lines {
        println!("{}", solve(&line));
    }

    Ok(())
}

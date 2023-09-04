use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res| res.unwrap().parse::<usize>().unwrap());

    let mut n = lines.next().unwrap() as usize;
    let mut l = lines.collect::<Vec<_>>();
    l.reverse();

    let mut res = 0;
    while !l.is_empty() {
        for i in 1..=100 {
            if let Some(&last) = l.last() {
                if i == last {
                    l.pop();
                }
            }
        }
        res += 1;
    }

    println!("{}", res);

    Ok(())
}

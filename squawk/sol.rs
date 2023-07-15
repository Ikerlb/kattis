use std::collections::VecDeque;
use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let lines = io::stdin()
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;
    let mut first = lines[0]
        .split(" ")
        .map(|x| x.parse::<usize>().unwrap());
    let n = first.next().unwrap();
    let m = first.next().unwrap();
    let s = first.next().unwrap();
    let t = first.next().unwrap();

    let mut g: Vec<Vec<usize>> = vec![Vec::new(); n];

    for i in 1..=m {
        let mut con = lines[i]
            .split(" ")
            .map(|x| x.parse::<usize>().unwrap());
        let n1 = con.next().unwrap();
        let n2 = con.next().unwrap();

        g[n1].push(n2);
        g[n2].push(n1);
    }

    let mut level = vec![0; n];
    level[s] = 1;

    for _ in 0..t {
        let mut nlevel = vec![0; n];
        for i in 0..level.len() {
            if level[i] > 0 {
                for nn in &g[i] {
                    nlevel[*nn] += level[i];
                }
            }
        }
        level = nlevel;
    }

    println!("{}", level.iter().sum::<usize>());

    Ok(())
}

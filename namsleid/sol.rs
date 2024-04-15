use std::io::{self, BufRead};
use std::collections::VecDeque;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|line_res| line_res.unwrap());

    let n = lines.next().unwrap().parse::<usize>().unwrap();
    let mut g = vec![Vec::new(); n];
    let mut incoming = vec![0; n];
    for (i, line) in lines.enumerate() {
        let mut iter = line
            .split(" ")
            .map(|nn| nn.parse::<usize>().unwrap());
        iter.next().unwrap();
        for nn in iter {
            incoming[i] += 1;
            g[nn - 1].push(i);
        }
    }

    let mut q = (0..n)
        .filter(|&i| incoming[i] == 0)
        .collect::<VecDeque<_>>();
    let mut level = 0;
    let mut levels = Vec::new();
    let mut elems = 0;
    while !q.is_empty() {
        if levels.len() == level {
            levels.push(Vec::new());
        }
        let elems_this_level = q.len();
        for _ in 0..elems_this_level {
            let n = q.pop_front().unwrap();
            levels[level].push(n);
            elems += 1;
            for &nn in &g[n] {
                 if incoming[nn] == 1 {
                    q.push_back(nn);
                }
                incoming[nn] -= 1;
            }
        }
        level += 1;

    }

    if elems == n {
        println!("Mogulegt!");
        println!("{}", levels.len());
        for v in levels {
            let vec = v
                .iter()
                .map(|n| format!("{}", n + 1))
                .collect::<Vec<_>>();
            let line = vec.join(" ");
            println!("{} {}", vec.len(), line);
        }
    } else {
        println!("Omogulegt!");
    }   

    Ok(())
}

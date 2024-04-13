use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());
    let binding = lines.next().unwrap();
    let mut first = binding.split(" ");
    let n = first.next().unwrap().parse::<usize>().unwrap();
    let q = first.next().unwrap().parse::<usize>().unwrap();

    let mut res = Vec::new();
    for line in lines.by_ref().take(n) {
        let mut binding = line.split(" ");
        let n1 = binding.next().unwrap().clone();
        let n2 = binding.next().unwrap().clone();
        res.push(n1);
        res.push(n2);
    }

    Ok(())
}

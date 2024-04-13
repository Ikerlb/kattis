use std::io::{self, BufRead};
use std::collections::HashMap;

#[derive(Debug)]
enum MartialStatus {
    Married,
    Unmarried,
    Unknown,
}

fn solve(hm: HashMap<String, MartialStatus>, lines: Vec<(String)>) -> String {
    for (s1, s2) in 0..l {
        match (s1, s2) {
            (MartialStatus::Married, MartialStatus::Unmarried) => {
                return "0".to_string();
            },
            (MartialStatus::Unmarried, MartialStatus::Married) => {
                continue;
            }
        };
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let mut handler = lines.next().unwrap();
    let mut first = handler.split(" ").map(|s| s.parse::<usize>().unwrap());

    let n = first.next().unwrap();
    let l = first.next().unwrap();

    let mut hm: HashMap<String, MartialStatus> = HashMap::new();

    for _ in 0..n {
        let line = lines.next().unwrap();
        let mut split = line.split(" ");
        let name = split.next().unwrap();
        let status = match split.next() {
            Some("m") => MartialStatus::Married,
            Some("u") => MartialStatus::Unmarried,
            _         => MartialStatus::Unknown,
        };

        hm.insert(name.to_string(), status);
    }

    let looking = lines
        .map(|line| {
            let split = line.split(" -> ");
            let s1 = hm[split.next().unwrap()];
            let s2 = hm[split.next().unwrap()];
            return (s1, s2);
        })
        .collect::<Vec<_>>();

    Ok(())
}

use std::io::{self, BufRead};
use std::str::FromStr;
use std::collections::BinaryHeap;
use std::cmp::Ordering;

#[derive(Debug, Eq, Clone)]
struct Runner {
    name: String,
    first: u64,
    second: u64,
}

impl Ord for Runner {
    fn cmp(&self, other: &Self) -> Ordering {
        self.second.cmp(&other.second)
    }
}

impl PartialOrd for Runner {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Runner {
    fn eq(&self, other: &Self) -> bool {
        self.second == other.second
    }
}

#[derive(Debug, PartialEq, Eq)]
struct ParseRunnerError;

// TODO: better error handling!
impl FromStr for Runner {
    type Err = ParseRunnerError;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let mut split = s.split(" ");

        let name = split
            .next()
            .unwrap();
        let first = split
            .next()
            .unwrap()
            .replace(".", "")
            .parse::<u64>()
            .unwrap();
        let second = split
            .next()
            .unwrap()
            .replace(".", "")
            .parse::<u64>()
            .unwrap();

        Ok(Runner {
            name: name.to_string(),
            first: first,
            second: second,
        })
    }
}
 

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let n = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    let runners = lines
        .map(|line_res| Runner::from_str(&line_res.unwrap()).unwrap())
        .collect::<Vec<_>>();

    let mut best_team = Vec::new();
    let mut best_so_far = u64::MAX;

    for first_leg in 0..n {
        let mut h = BinaryHeap::new();
        for rest in 0..n {
            if rest == first_leg {
                continue;
            }
            if h.len() < 3 {
                h.push(runners[rest].clone());
            } else if runners[rest] < *h.peek().unwrap() {
                h.pop();
                h.push(runners[rest].clone());
            }
        }
        let s = h
            .iter()
            .map(|r| r.second)
            .sum::<u64>() + runners[first_leg].first;
        if s < best_so_far {
            best_so_far = s;
            best_team = vec![runners[first_leg].clone()];
            best_team.extend(h);
        }
    }

    let decimals = best_so_far % 100;
    let wholes = best_so_far / 100;

    println!("{}.{:0>2}", wholes, decimals);
    for runner in best_team {
        println!("{}", runner.name);
    }

    Ok(())
}

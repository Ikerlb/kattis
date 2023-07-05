use std::iter::FilterMap;
use std::io::{self, BufRead};

fn parse_state(lines: &Vec<String>) -> Vec<Vec<char>> {
    lines
        .iter()
        .map(|line| line.chars().collect())
        .collect()
}

fn dfs(state: &Vec<Vec<char>>, x: usize, y: usize) -> usize {
    
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .filter_map(|line| line.ok());

    // burn 'first'
    lines.next();

        let tt = parse_state(&lines.take(3).collect());

    Ok(())
}

use std::collections::HashSet;
use std::io::{self, BufRead};

fn dfs(b: &mut Vec<Vec<char>>, r: isize, c: isize, path: &mut Vec<char>, depth: i8, res: &mut HashSet<String>, words: &HashSet<String>) {
    if depth < 0 {
        return;
    }

    path.push(b[r as usize][c as usize]);
    let s = path.iter().collect::<String>();
    if words.contains(&s) {
        res.insert(s);
    }

    let n = b.len() as isize;
    let m = b[0].len() as isize;

    let prev = b[r as usize][c as usize];
    b[r as usize][c as usize] = '#';

    for dr in -1isize..=1isize {
        for dc in -1isize..=1isize {
            if dr == 0 && dc == 0 {
                continue;
            } else if r + dr < 0 || r + dr == n {
                continue;
            } else if c + dc < 0 || c + dc == m {
                continue;
            } else if b[(r + dr) as usize][(c + dc) as usize] == '#' {
                continue;
            }
            dfs(b, r + dr, c + dc, path, depth - 1, res, words);
        }
    }

    path.pop();
    b[r as usize][c as usize] = prev;
}

fn score(n: usize) -> usize {
    match n {
        3|4 => 1,
        5   => 2,
        6   => 3,
        7   => 5,
        8   => 11,
        _   => 0
    }
}

fn format_solution(hs: HashSet<String>) -> String {
    let sum: usize = hs
        .iter()
        .map(|x| score(x.len()))
        .sum();
    let max_length = hs
        .iter()
        .map(|x| x.len())
        .max()
        .unwrap();
    let mut same = hs
        .iter()
        .filter(|x| x.len() == max_length)
        .collect::<Vec<_>>();
    same.sort();
    let biggest = same[0];
    let num = hs.len();
    return format!("{} {} {}", sum, biggest, num);
}

fn solve(mut b: Vec<Vec<char>>, words: &HashSet<String>) -> String {
    let mut res = HashSet::new();
    let mut path = Vec::new();
    for row in 0..b.len() {
        for col in 0..b[0].len() {
            dfs(&mut b, row as isize, col as isize, &mut path, 8i8, &mut res, words);
        }
    }
    return format_solution(res);
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let num_words = lines.next().unwrap()?.parse::<usize>().unwrap();

    let words = (0..num_words)
        .map(|_| lines.next().unwrap().unwrap())
        .collect::<HashSet<String>>();

    lines.next();

    let num_boggles = lines.next().unwrap()?.parse::<usize>().unwrap();
    for i in 0..num_boggles {
        let boggle = (0..4)
            .map(|_| lines.next().unwrap().unwrap().chars().collect::<Vec<_>>())
            .collect::<Vec<_>>();
        println!("{}", solve(boggle, &words));
        if i != num_boggles - 1 {
            lines.next();
        }
    }

    Ok(())
}

use std::collections::HashSet;
use std::io::{self, BufRead};

fn f(c: char) -> i64 {
    return ((c as i64) - ('a' as i64)) + 1;
}

fn pow(a: i64, b: usize, p: i64) -> i64 {
    if b == 0 {
        return 1;
    }
    let half = pow(a, b >> 1, p);
    if b % 2 == 0 {
        return (half * half) % p;
    } else {
        return (((half * half) % p) * a) % p;
    }
}

fn modulo(n: i64, m: i64) -> i64 {
    return ((n % m) + m) % m;
}

fn hash(s: &Vec<char>, p: i64) -> i64 {
    let mut h = 0;
    let n = s.len();
    for i in (0..n) {
        h = (h + modulo(f(s[i]) * pow(31, i, p), p)) % p;
    }
    return h;
}

fn hashes(s: &Vec<char>, p: i64) -> Vec<i64> {
    let mut res = Vec::new();

    if s.is_empty() {
        return res;
    }

    let mut hl = hash(s, p); 
    let mut hr = 0;
    let n = s.len() - 1;

    let ps = s.iter().collect::<String>();

    for (i, &c) in s.iter().enumerate().rev() {
        hl -= (f(c) * pow(31, i, p)) % p;
        while hl < 0 {
            hl += p;
        }
        res.push((hl + hr) % p);
        hr = (hr + modulo(f(c) * pow(31, i - 1, p), p)) % p;
    }

    return res;
}

fn main() -> io::Result<()> {
    let mut lines = io::stdin()
        .lock()
        .lines()
        .map(|res| res.unwrap().chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>();

    let p = 100000004987i64;
    let hs = lines[1..]
        .iter()
        .map(|v| hash(v, p))
        .collect::<HashSet<i64>>();

    let mut res = Vec::new();
    for v in &lines[1..] {
        hashes(v, p)
            .iter()
            .any(|x| hs.contains(x))
            .then(|| {
                res.push(v.iter().collect::<String>());
            });
    }
    if res.len() > 0 {
        println!("{}", res.join("\n"));
    } else {
        println!("NO TYPOS");
    }

    return Ok(());
}

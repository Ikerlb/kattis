use std::io::{self, BufRead};

fn step(previous_hash: i64, s: &str) -> i64 {
    let mut v = previous_hash;
    for c in s.chars() {
        v = (v * 31 + (c as i64)) % 1000000007;
    }
    return v * 7 % 1000000007;
}

fn possible(max: i64, trailing: usize) -> Vec<i64>{
    let s = format!("{}", max)
        .chars()
        .collect::<String>();
    let (head, rest) = s.split_at(s.len() - trailing);
    let mut n = head.parse::<i64>().unwrap();
    if rest.parse::<i64>().unwrap() > 0 {
        n += 1;
    }
    
    let pad = "0".repeat(trailing);

    (0..n)
        .map(|i| format!("{}{}", i, pad).parse::<i64>().unwrap())
        .collect::<Vec<_>>()
}

fn H(previous_hash: i64, transaction: &str, token: i64) -> i64 {
    let v_prime = step(previous_hash, transaction);
    return (v_prime + token) % 1000000007;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();
    let mut previous_hash = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<i64>()
        .unwrap();

    let poss = possible(1000000007, 7);

    let st1 = "charlie-pays-to-eve-9-sg-coins".to_string();
    let st2 = "icpc-sg-2018-at-nus".to_string();

    let s1 = step(previous_hash, &st1);
    let p1 = poss
        .iter()
        .filter_map(|h| {
            if h - s1 < 0 {
                None
            } else {
                Some(h - s1)
            }
        })
        .next()
        .unwrap();

    previous_hash = H(previous_hash, &st1, p1);
    let s2 = step(previous_hash, &st2);
    let p2 = poss
        .iter()
        .filter_map(|h| {
            if h - s2 < 0 {
                None
            } else {
                Some(h - s2)
            }
        })
        .next()
        .unwrap();

    println!("{} {}", st1, p1);
    println!("{} {}", st2, p2);

    Ok(())
}

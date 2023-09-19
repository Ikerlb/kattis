use std::io::{BufRead, self};
use std::collections::HashMap;
use std::cmp::Ordering;

#[derive(Debug, Clone, Eq)]
struct CounterEntry {
    freq: usize,
    index: usize 
}

impl Ord for CounterEntry {
    fn cmp(&self, other: &Self) -> Ordering {
        (self.index, self.freq).cmp(&(other.index, other.freq))
    }
}

impl PartialOrd for CounterEntry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for CounterEntry {
    fn eq(&self, other: &Self) -> bool {
        self.freq == other.freq && self.index == other.index
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    while let Some(line_res) = lines.next() {
        let m = line_res.unwrap().parse::<usize>().unwrap();
        if m == 0 {
            break;
        }
        let line = lines
            .next()
            .unwrap()
            .unwrap();
        let s = line
            .chars()
            .map(|c| (c as i64 - 'a' as i64) + 1)
            .collect::<Vec<_>>();
        let base = 31;
        //let p = 972663749;
        let p = 614889782588491410;
        //let p = 1000000007;
        println!("{}", solve(&s, m, base, p));
    }

    Ok(())    
}

fn pow(a: i64, b: usize, p: i64) -> i64 {
    if b == 0 {
        return 1;
    } else if b & 1 == 0 {
        let half = pow(a, b >> 1, p);
        return prod(half, half, p);
    } else {
        let half = pow(a, b >> 1, p);
        return prod(prod(half, half, p), a, p);
    }
}

fn hash(s: &[i64], b: i64, p: i64) -> i64 {
    let mut h: i64 = 0;
    for (i, &c) in s.iter().rev().enumerate() {
        h = (h + prod(c, pow(b, i, p), p)) % p;
    }
    return h;
}

fn modulo(n: i64, m: i64) -> i64 {
    // ((n % M) + M) % M   
    //return ((n % m).wrapping_add(m)) % m;
    return ((n % m) + m) % m;
}

fn prod(a: i64, b: i64, m: i64) -> i64 {
    let pu = a as i128 * b as i128;
    let mu = m as i128; 
    return (pu % mu) as i64;
}

fn hashes_brute(s: &Vec<i64>, k: usize, b: i64, p: i64) -> Vec<i64> {
    let n = s.len();
    let mut res = Vec::new();
    for i in 0..=(n - k) {
        res.push(hash(&s[i..i + k], b, p));
    }
    return res;
}

fn hashes(s: &Vec<i64>, k: usize, b: i64, p: i64) -> Vec<i64> {
    let n = s.len();
    let mut res = Vec::new();
    let mut h = hash(&s[..k], b, p);
    res.push(h);
    for i in k..n {
        //h = (h - ((s[i - k] * pow(b, k - 1, p)) % p)) % p;
        //h = modulo(h - modulo(s[i  - k] * pow(b, k - 1, p), p), p);
        let pw = pow(b, k - 1, p);
        h = modulo(h - prod(s[i - k], pw, p), p);
        //h = (h * b) % p;
        h = prod(h, b, p);
        h = (h + s[i]) % p;
        res.push(h);
    }
    return res;
}

fn _try(s: &Vec<i64>, k: usize, m: usize, b: i64, p: i64) -> Option<usize>{
    let mut d: HashMap<i64, CounterEntry> = HashMap::new();
    for (i, &h) in hashes(s, k, b, p).iter().enumerate() {
        let entry = d.entry(h).or_insert(CounterEntry{freq: 0, index: 0});
        entry.freq += 1;
        entry.index = i;
    }
    let mut vals = d
        .values()
        .collect::<Vec<_>>();

    vals.sort();

    for v in vals.iter().rev() {
        if v.freq >= m {
            return Some(v.index)
        }
    }
    return None;

    /*for k in d.keys() {
        let v = d.get(k).unwrap();
        if v.freq >= m {
            return Some(v.index);
        }
    }
    return None;*/
}

fn solve(s: &Vec<i64>, m: usize, b: i64, p: i64) -> String {
    let mut l = 1;
    let mut r = s.len();

    let mut res = None;

    while l <= r {
        let mid = (l + r) >> 1;
        if let Some(t) = _try(s, mid, m, b, p) {
            res = Some((mid, t));
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    if let Some(res_tup) = res {
        return format!("{} {}", res_tup.0, res_tup.1);
    } else {
        return "none".to_string();
    }
}

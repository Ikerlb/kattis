use std::io::{self, BufRead};
use std::cmp::{min, max};

const BASE: u64 = 31;
const PRIME: u64 = 614889782588491410;

fn prod(a: u64, b: u64, p: u64) -> u64 {
    let res = (a as u128 * b as u128) % p as u128;
    return res as u64;
}

fn pow(mut a: u64, mut b: u64, p: u64) -> u64 {
    let mut res = 1;
    while b > 0 {
        if b & 1 == 1 {
            res = prod(res, a, p);
        }
        b >>= 1;
        a = prod(a, a, p);
    }
    return res;
}

fn hash(v: &[u64], b: u64, prime: u64) -> u64 {
    let mut s = 0;
    for i in 0..v.len() {
        s = (s + (v[i] * pow(b, i as u64, prime))) % prime;
    }
    return s;
}

struct SegmentTree {
    tree: Vec<u64>,
    arr: Vec<u64>,
    pows: Vec<u64>
}

impl SegmentTree {
    fn childs(v: usize, mid: usize, l: usize) -> (usize, usize) {
        let left = v + 1;
        let right = v + 2 * (mid - l + 1);
        return (left, right);
    }

    fn new(arr: Vec<u64>) -> Self {
        let n = arr.len();

        let mut pows = vec![1; n];

        for i in 1..n {
            pows[i] = prod(pows[i - 1], BASE, PRIME);
        }

        let mut st = Self {
            tree: vec![0; n * 2],
            arr: arr,
            pows: pows,
        };

        st.build(1, 0, n - 1);

        return st;
    }

    fn build(&mut self, i: usize, l: usize, r: usize) -> u64 {
        if l == r {
            self.tree[i] = self.arr[l];
            return self.tree[i];
        }
        let mid = (l + r) >> 1;
        let (li, ri) = Self::childs(i, mid, l);

        let left =  self.build(li, l, mid);
        let right = self.build(ri, mid + 1, r);

        let off = mid - l + 1;
        //let res = (left + prod(right, pow(BASE, off, PRIME), PRIME)) % PRIME;
        let res = (left + prod(right, self.pows[off], PRIME)) % PRIME;

        self.tree[i] = res;
        return res;
    }

    fn query(&self, l: usize, r: usize) -> u64 {
        let n = self.arr.len();
        return self.query_range(1, 0, n - 1, l, r);
    }

    fn query_range(&self, i: usize, tl: usize, tr: usize, l: usize, r: usize) -> u64 {
        if l > r {
            return 0;
        }
        if tl == l && tr == r {
            return self.tree[i];
        }
        let tm = (tl + tr) >> 1;

        let llim = min(r, tm);
        let rlim = max(l, tm + 1);

        let (li, ri) = Self::childs(i, tm, tl);

        let left = self.query_range(li, tl, tm, l, llim);
        let right = self.query_range(ri, tm + 1, tr, rlim, r);

        let off = if llim >= l {
            llim - l + 1
        } else {
            0
        };

        //let res = (left + prod(right, pow(BASE, off, PRIME), PRIME)) % PRIME;
        let res = (left + prod(right, self.pows[off], PRIME)) % PRIME;

        //println!("is at ({}, {}) left {} right {}", tl, tr, left, right);
        //println!("h({}, {}) -> {}", l, r, res);

        return res;
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let v = lines
        .next()
        .unwrap()
        .unwrap()
        .chars()
        .map(|c| c as u64 - 'a' as u64 + 1)
        .collect::<Vec<_>>(); 

    let qs = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    let queries = lines
        .map(|s_res| {
            let handler = s_res
                .unwrap();
            let mut split = handler
                .split(" ") 
                .map(|ns| ns.parse::<usize>().unwrap());
            let first = split.next().unwrap();
            let second = split.next().unwrap();
            return (first, second);
        });

    let mut st = SegmentTree::new(v);

    for (i, j) in queries {
        println!("{}", st.query(i, j - 1));
    }
    
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn segment_tree_ok() {
        let s = "babbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbabbabbababbabbab".to_string();
        let v = s
            .chars()
            .map(|c| c as u64 - 'a' as u64 + 1)
            .collect::<Vec<_>>();

        let n = v.len();

        println!("{:?}", v);

        let st = SegmentTree::new(v.clone());

        for i in 0..n {
            for j in i..n {
                let is = st.query(i, j);
                let should_be = hash(&v[i..=j], BASE, PRIME);
                println!("i = {}, j = {}", i, j);
                println!("is {} but should be {}", is, should_be);
                assert_eq!(is, should_be)
            }
        }
    }
}

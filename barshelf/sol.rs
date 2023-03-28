use std::io::{self, BufRead};
use std::collections::{ HashSet, HashMap };
use std::fmt::{Formatter, Debug, self};

struct FenwickTree {
    tree: Vec<isize>,
}

impl FenwickTree {
    fn new(n: usize) -> Self {
        Self {
            tree: vec![0; n + 1],
        }
    }

    fn add(&mut self, mut i: isize, x: isize) {
        i += 1;
        while i < (self.tree.len() as isize) {
            self.tree[i as usize] += x;
            i += i & -i;
        }
    }

    fn sum(&self, mut i: isize) -> isize {
        let mut s = 0;
        while i > 0 {
            s += self.tree[i as usize];
            i -= i & -i;
        }
        s
    }

    fn query(&self, l: isize, r: isize) -> isize {
        let r = self.sum(r + 1);
        let l = self.sum(l);
        r - l
    }
}

impl Debug for FenwickTree {
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let mut v = Vec::new();
        for i in 0..(self.tree.len() - 1) {
            v.push(format!("0 {} -> {}", i, self.query(0, i as isize)));
        }
        write!(f, "{:?}", v)
    }
}


fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let n = lines.next().unwrap()?.parse::<usize>().unwrap();
    let heights = lines
        .next()
        .unwrap()?
        .split_whitespace()
        .map(|x| x.parse::<isize>().unwrap())
        .collect::<Vec<isize>>();

    let hs = heights
        .iter()
        .map(|&i| i)
        .collect::<HashSet<isize>>();

    let mut s = hs
        .iter()
        .map(|&i| i)
        .collect::<Vec<isize>>();

    s.sort();

    let d = s
        .iter()
        .enumerate()
        .map(|(i, &x)| (x, i as isize))
        .collect::<HashMap<isize, isize>>();

    let mut left = FenwickTree::new(n);
    let mut rite = FenwickTree::new(n);

    heights
        .iter()
        .for_each(|&h| rite.add(d[&h], 1));

    let mut res = 0;
    for n in heights {
        rite.add(d[&n], -1);
        let ri = match s.binary_search(&(n >> 1)) {
            Ok(i) => i as isize,
            Err(i) => i as isize - 1,
        };

        let li = match s.binary_search(&(n << 1)) {
            Ok(i) => i as isize,
            Err(i) => i as isize,
        };

        let r = rite.query(0, ri);
        let l = left.query(li, (s.len() - 1) as isize);

        res += r * l;
        left.add(d[&n], 1);
    }

    println!("{}", res);

    Ok(())
}

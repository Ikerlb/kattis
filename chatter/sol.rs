use std::collections::{HashMap, HashSet};
use std::io::{self, Result, BufRead, BufWriter, Write};
use std::mem::swap;

struct Ufs {
    parents: Vec<usize>
}

impl Ufs {
    pub fn new(n: usize) -> Self {
        Self {
            parents: (0..n).collect::<Vec<_>>(),
        }
    }

    fn root(&mut self, a: usize) -> usize {
        if a == self.parents[a] {
            return a;
        } else {
            let ra = self.root(self.parents[a]);
            self.parents[a] = ra;
            return ra;
        }
    }

    fn union(&mut self, a: usize, b: usize) -> bool {
        let mut ra = self.root(a);
        let mut rb = self.root(b);

        if ra == rb {
            return false;
        }

        self.parents[ra] = rb;
        return true;
    }

    fn groups(&mut self) -> Vec<(usize, usize)> {
        let mut g = HashMap::new();
        for i in 0..self.parents.len() {
            *g.entry(self.root(i)).or_insert(0) += 1;
        }
        return g
            .drain()
            .map(|(k, v)| (v, k))
            .collect();
    }
}

/*fn random(r: &mut usize, a: usize, b: usize, c: usize) -> usize {
    let nr = (*r * a) + b % c;
    *r = nr;
    return nr;
}*/

fn random(r: &mut usize, a: usize, b: usize, c: usize) -> usize {
    let nr = ((*r * a) + b) % c;
    *r = nr;
    return nr;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();

    let mut writer = BufWriter::new(stdout.lock());

    let lines = stdin
        .lock()
        .lines()
        .collect::<Result<Vec<_>>>()?;

    for line in lines.iter() {
        let mut iter = line
            .split(" ")
            .map(|s| s.parse::<usize>().unwrap());

        let n = iter.next().unwrap();
        let mut r = iter.next().unwrap();
        let a = iter.next().unwrap();
        let b = iter.next().unwrap();
        let c = iter.next().unwrap();

        let mut ufs = Ufs::new(n);

        for i in 0..n {
            let mut x = random(&mut r, a, b, c) % n;
            let mut y = random(&mut r, a, b, c) % n;
            while x == y {
                x = random(&mut r, a, b, c) % n;
                y = random(&mut r, a, b, c) % n;
            }
            ufs.union(x, y);
            
        }
        let groups = ufs.groups();
        let mut counts = HashMap::new();
        for &(s, _) in &groups {
            *counts.entry(s).or_insert(0) += 1;
        }
        let mut vcounts = counts
            .drain()
            .collect::<Vec<_>>();
        vcounts.sort();
        let res = vcounts
            .iter()
            .rev()
            .map(|&(c, cc)| if cc == 1 {
                format!("{}", c)
            } else {
                format!("{}x{}", c, cc)
            })
            .collect::<Vec<_>>();
        write!(writer, "{} {}\n", groups.len(), res.join(" "));
    }

    Ok(())
}

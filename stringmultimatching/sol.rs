use std::io::{self, BufRead, BufWriter, Write};
use std::cmp::Ordering;
use std::mem::swap;
use std::iter;

#[derive(Debug, Clone, Eq)]
struct Entry {
    fst: isize,
    snd: isize,
    p: usize,
}

impl Entry {
    fn new(fst: isize, snd: isize, p: usize) -> Self {
        return Self {
            fst: fst,
            snd: snd,
            p: p,
        };
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        return self.fst == other.fst && self.snd == other.snd;
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        return Some(self.cmp(other));
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        return (self.fst, self.snd).cmp(&(other.fst, other.snd));
    }
}

fn create_suffix_array(s: &Vec<char>) -> Vec<usize> {
    let n = s.len();
    let mut ra = s
        .iter()
        .map(|&c| c as usize)
        .collect::<Vec<_>>();
    let mut nra = vec![0; n];
    let mut l = vec![Entry::new(0, 0, 0); n];
    let mut k = 1;
    while k <= n {
        for i in 0..n {
            l[i].fst = ra[i] as isize;
            l[i].snd = if i + k < n {
                ra[i + k] as isize
            } else {
                -1
            };
            l[i].p = i;
            nra[i] = 0;
        }

        l.sort();

        for i in 1..n {
            nra[l[i].p] = if l[i] == l[i - 1] {
                nra[l[i - 1].p]
            } else {
                i
            };
        }

        swap(&mut ra, &mut nra);
        k *= 2;
    }

    return l
        .iter()
        .map(|e| e.p)
        .collect();
}

fn compare(s: &Vec<char>, si: usize, p: &str) -> Ordering {
    let mut siter = s[si..]
        .iter()
        .chain(iter::repeat(&'\x1b'));
    let mut piter = p.chars();
    for (&c1, c2) in siter.zip(piter) {
        if c1 < c2 {
            return Ordering::Less;
        } else if c1 > c2 {
            return Ordering::Greater;
        }
    }
    return Ordering::Equal;
}

/*  */
fn find(s: &Vec<char>, sa: &Vec<usize>, p: &str) -> Vec<usize> {
    let mut l = 0 as isize;
    let mut r = (sa.len() - 1) as isize;
    let mut lres = -1;

    while l <= r {
        let m = (l + r) >> 1;
        match compare(s, sa[m as usize], p) {
            Ordering::Greater | Ordering::Equal => {
                lres = m;
                r = m - 1;
            }, 
            Ordering::Less => {
                l = m + 1;
            },
        }
    }


    let left = lres as usize;

    if lres == -1 || compare(s, sa[left], p) != Ordering::Equal {
        return Vec::new();
    }

    l = lres;
    r = (sa.len() - 1) as isize;
    let mut rres = -1;

    while l <= r {
        let m = (l + r) >> 1;
        match compare(s, sa[m as usize], p) {
            Ordering::Greater => {
                r = m - 1;
            }, 
            Ordering::Less | Ordering::Equal => {
                l = m + 1;
                rres = m as isize;
            },
        }
    }

    let mut res = (left..=rres as usize)
        .map(|i| sa[i])
        .collect::<Vec<usize>>();

    res.sort();

    return res;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut lines_v = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;

    let mut lines = lines_v.drain(..);

    let mut writer = BufWriter::new(stdout);

    while let Some(n_s) = lines.next() {
        let n = n_s.parse::<usize>().unwrap();
        let mut patterns = Vec::with_capacity(n);
        for _ in 0..n {
            patterns.push(lines.next().unwrap());
        }
        let s = lines
            .next()
            .unwrap()
            .chars()
            .collect::<Vec<_>>();
        let sa = create_suffix_array(&s);
        for p in patterns {
            let mut v = find(&s, &sa, &p);
            let sv = v
                .drain(..)
                .map(|i| i.to_string())
                .collect::<Vec<_>>();
            writeln!(writer, "{}", sv.join(" "));
        }
    }

    Ok(())
}

use std::io::{self, BufRead};
use std::mem::swap;
use std::cmp::{Ordering, max};

#[derive(Debug, Clone, Eq)]
struct Entry {
    fst: isize,
    snd: isize,
    p: usize,
}

impl Entry {
    fn new(fst: isize, snd: isize, p: usize) -> Self {
        return Entry{
            fst: fst,
            snd: snd,
            p: p
        };
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        (self.fst, self.snd) == (other.fst, other.snd)
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        (self.fst, self.snd).cmp(&(other.fst, other.snd))
    }
}

fn create_suffix_array(v: &Vec<char>) -> Vec<usize> {
    let mut ra = v
        .iter()
        .map(|&c| c as usize)
        .collect::<Vec<usize>>();
    let n = ra.len();
    let mut nra = vec![0; n];
    let mut l = vec![Entry::new(0, 0, 0); n];

    let mut k = 1;
    while k <= n {
        for i in 0..n {
            l[i].fst = ra[i] as isize;
            l[i].snd = ra[(i + k) % n] as isize;
            l[i].p = i;
            nra[i] = 0;
        }

        l.sort();

        for i in 1..n {
            if l[i] == l[i - 1] {
                nra[l[i].p] = nra[l[i - 1].p];
            } else {
                nra[l[i].p] = i;
            }
        }

        swap(&mut ra, &mut nra);

        k *= 2;
    }

    return l
        .iter()
        .map(|e| e.p)
        .collect();
}

fn create_lcp_array(v: &Vec<char>, sa: &Vec<usize>) -> Vec<usize> {
    let n = v.len();
    // previous index in sa!
    let mut phi = vec![-1; n];

    for i in 1..n {
        phi[sa[i]] = sa[i - 1] as isize; 
    }

    let mut l = 0; 

    let mut plcp = vec![0; n];

    for i in 0..n {
        let p = phi[i];

        if p == -1 {
            continue;
        }

        let pu = p as usize;

        while i + l < n && pu + l < n && v[i+l] == v[pu+l] {
            l += 1;
        }
        plcp[i] = l;
        l = if l == 0 {
            0
        } else {
            l - 1
        };
    }
    let mut lcp = vec![0; n];
    for i in 0..n {
        lcp[i] = plcp[sa[i]];
    }
    return lcp;
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

    let s = lines
        .next()
        .unwrap()
        .unwrap()
        .chars()
        .collect::<Vec<char>>();

    let sa = create_suffix_array(&s);
    let lcp = create_lcp_array(&s, &sa);

    println!("{}", lcp.iter().max().unwrap());

    Ok(())
}

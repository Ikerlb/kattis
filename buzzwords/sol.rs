use std::io::{self, BufRead};
use std::cmp::{Ordering, min, max};
use std::mem::swap;


#[derive(Debug, Clone, Eq)]
struct Entry {
    fst: isize, 
    snd: isize, 
    p: usize,
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

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        self.fst == other.fst && self.snd == other.snd
    }
}

impl Entry {
    fn new(fst: isize, snd: isize, p: usize) -> Self {
        Entry {
            fst: fst,
            snd: snd,
            p: p
        }
    }
}

fn build_suffix_array(s: &Vec<char>) -> Vec<usize> {
    let n = s.len();
    let mut ra = s
        .iter()
        .map(|&c| c as isize)
        .collect::<Vec<_>>();
    let mut nra = vec![0isize; n];
    let mut l = vec![Entry::new(0, 0, 0); n];
    let mut k = 1;


    while k < n {
        for i in 0..n {
            let fst = ra[i];
            let snd = if i + k < n {
                ra[i + k]
            } else {
                -1
            };
            l[i].fst = fst;
            l[i].snd = snd;
            l[i].p = i;

            nra[i] = 0;
        }

        l.sort();

        nra[l[0].p] = 0;
        for i in 1..n {
            nra[l[i].p] = if l[i] == l[i - 1] {
                nra[l[i - 1].p]
            } else {
                i as isize
            }
        }
        k <<= 1;
        swap(&mut ra, &mut nra);
    }
    return l
        .iter()
        .map(|e| e.p)
        .collect();
}

fn solve(lcp: &Vec<usize>) -> Vec<String> {
    let mut res = Vec::new();
    for cnt in 1..lcp.len() {
        let mut cur = 0;
        let mut maxi = 0;
        for j in 0..lcp.len() {
            if lcp[j] >= cnt {
                cur += 1;
                maxi = max(maxi, cur);
            } else {
                cur = 0;
            }
        }
        if maxi == 0 {
            break;
        } else {
            res.push(format!("{}", maxi + 1));
        }
    }
    return res;
}

fn build_lcp_array(t: &Vec<char>, sa: &Vec<usize>) -> Vec<usize> {
    let n = t.len();
    let mut phi = vec![0isize; n];
    let mut plcp = vec![0; n];

    phi[sa[0]] = -1;
    for i in 1..n {
        phi[sa[i]] = sa[i - 1] as isize;
    }
    let mut l = 0;
    for i in 0..n {
        if phi[i] == -1 {
            plcp[i] = 0;
            continue;
        }
        while (i + l < n) && (phi[i] as usize + l < n) && (t[i + l] == t[phi[i] as usize + l]) {
            l += 1;
        }
        plcp[i] = l;
        l = if l == 0 {
            0
        } else {
            l - 1
        };
    }
    return (0..n)
        .map(|i| plcp[sa[i]])
        .collect();
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let lines = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;
    for line in &lines[..lines.len() - 1] {
        let v = line
            .chars()
            .filter(|&c| c != ' ')
            .collect();
        let sa = build_suffix_array(&v);
        let lcpa = build_lcp_array(&v, &sa);
        println!("{}", solve(&lcpa).join("\n"));
        println!();
    }
    Ok(())
}

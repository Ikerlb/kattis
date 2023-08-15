use std::io::{BufRead, self};
use std::cmp::Ordering;
use std::mem::swap;

#[derive(Debug, Clone, Eq)]
struct Entry {
    fst: isize,
    snd: isize,
    p: usize,
}

impl Entry {
    fn new(fst: isize, snd: isize, p: usize) -> Self {
        Self {
            fst: fst,
            snd: snd,
            p: p,
        }
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        (self.fst, self.snd).cmp(&(other.fst, other.snd))
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        self.fst == other.fst && self.snd == other.snd
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
            l[i].fst = ra[i];
            l[i].snd = if i + k < n{
                ra[i + k]
            } else {
                -1
            };
            l[i].p = i;
            nra[i] = 0;
        }

        l.sort();

        nra[l[0].p] = 0;
        for i in 1..n {
            nra[l[i].p] = if l[i - 1] == l[i] {
                nra[l[i - 1].p]
            } else {
                i as isize
            }
        }

        swap(&mut ra, &mut nra);
        k <<= 1;
    }
    return l
        .iter()
        .map(|e| e.p)
        .collect();
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
        let s = lines
            .next()
            .unwrap()
            .unwrap();
        let v = s
            .chars()
            .collect::<Vec<_>>();
        let sa = build_suffix_array(&v);
        println!("{:?} {:?}", v, sa);
    }

    Ok(())
}

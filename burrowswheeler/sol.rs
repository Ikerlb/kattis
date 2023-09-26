use std::io::{self, BufRead};
use std::mem::swap;
use std::cmp::Ordering;

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

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    for line in lines {
        let mut v = line
            .chars()
            .collect::<Vec<_>>();
        let mut sa = create_suffix_array(&v);

        /*for &si in &sa {
            let start = &line[si..].chars().collect::<String>();
            let end = &line[..si].chars().collect::<String>();
            println!("{}{}", start, end);
        }*/

        let res = sa
            .iter()
            .map(|&i| if i == 0 {
                *v.last().unwrap()
            } else {
                v[i - 1]
            })
            .collect::<String>();
        println!("{}", res);
    }

    Ok(())
}

use std::io::{self, BufRead};
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
        return Self {
            fst: fst,
            snd: snd,
            p: p
        };
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        return (self.fst, self.snd).cmp(&(other.fst, other.snd));
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        return Some(self.cmp(other));
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        return self.fst == other.fst && self.snd == other.snd;
    }
}

fn create_lcp_array(s: &Vec<char>, sa: &Vec<usize>) -> Vec<usize> {
    let n = s.len();
    let mut phi: Vec<isize> = vec![-1; n];
    
    for i in 1..n {
        phi[sa[i]] = sa[i - 1] as isize;
    }

    let mut l = 0;
    let mut nlcp = vec![0; n];
    
    for i in 0..n {
        let p = phi[i];

        if p == -1 {
            continue;
        }

        let pu = p as usize;

        while i + l < n && pu + l < n && s[i+l] == s[pu+l] {
            l += 1;
        }

        nlcp[i] = l;

        l = if l == 0 {
            0
        } else {
            l - 1
        };
    }

    let mut lcp = vec![0; n];
    for i in 0..n {
        lcp[i] = nlcp[sa[i]];
    }
    return lcp;
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
        .lines();

    let s = lines
        .next()
        .unwrap()
        .unwrap()
        .chars()
        .collect::<Vec<_>>();

    let sa = create_suffix_array(&s);
    let lcp = create_lcp_array(&s, &sa);
    let mx = *lcp.iter().max().unwrap();

    let mut res = "".to_string();

    /* we go over the sa to get it in lexicographical order */
    for i in 1..s.len() {
        if lcp[i] == mx {
            res = s[sa[i]..sa[i] + mx]
                .iter()
                .collect::<String>();
            break;
        }
    }

    println!("{}", res);

    /*for &i in &sa {
        let ss = s[i..]
            .iter()
            .map(|&u| (u as u8) as char)
            .collect::<String>();
        println!("{} {}", i, ss);
    }*/

    Ok(())
}

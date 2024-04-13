use std::cmp::Ordering;
use std::mem::swap;
use std::io::{self, BufRead, BufWriter, Write};

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

/* almost 1 second faster with sort unstable!! */
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

        l.sort_unstable();

        for i in 1..n {
            nra[l[i].p] = if l[i - 1] == l[i] {
                nra[l[i - 1].p]
            } else {
                i
            };
        }
        
        swap(&mut ra, &mut nra);
        k <<= 1;
    }

    return l
        .iter()
        .map(|e| e.p)
        .collect();
}

fn create_lcp_array(v: &Vec<char>, sa: &Vec<usize>) -> Vec<usize> {
    let n = sa.len();
    let mut phi = vec![-1; n];
    for i in 1..n {
        phi[sa[i]] = sa[i - 1] as isize;  
    }

    let mut nlcp = vec![0; n];
    let mut l = 0;
    for i in 0..n {
        if phi[i] == -1 {
            continue;
        }
        let p = phi[i] as usize;
        while i + l < n && p + l < n && v[i+l] == v[p+l] {
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

fn format(v: &Vec<char>, sa: &Vec<usize>) -> String {
    let mut res = Vec::new();
    for &si in sa {
        let s = v[si..].iter().collect::<String>();
        res.push(s);
    }
    return res.join("\n");
}

fn solve(sa: &Vec<usize>, lcp: &Vec<usize>) -> usize {
    let n = sa.len();
    return (1..n)
        .map(|i| if lcp[i] > lcp[i - 1] {
            lcp[i] - lcp[i - 1]
        } else {
            0
        })
        .sum();
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout);
    let mut lines = stdin 
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let n = lines
        .next()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    for s in lines {
        let v = s
            .chars()
            .collect::<Vec<_>>();
        let sa = create_suffix_array(&v);
        let lcp = create_lcp_array(&v, &sa);
        writeln!(writer, "{}", solve(&sa, &lcp));
    }

    Ok(())
}

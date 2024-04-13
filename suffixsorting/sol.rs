use std::io::{self, BufRead};
use std::cmp::Ordering;
use std::mem::swap;

#[derive(Eq, Clone)]
struct Entry {
    first: isize,
    second: isize,
    p: usize,
}


impl Entry {
    fn new(first: isize, second: isize, p: usize) -> Self {
        return Self {
            first,
            second,
            p
        };
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        return (self.first, self.second).cmp(&(other.first, other.second));
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        return self.first == other.first && self.second == other.second;
    }
}

fn build(s: &Vec<char>) -> Vec<usize> {
    let n = s.len();
    let mut ra = s
        .iter()
        .map(|&c| c as isize)
        .collect::<Vec<_>>();

    let mut l = vec![Entry::new(0, 0, 0); n];

    let mut nra = vec![0isize; n];
    let mut cnt = 1;

    while cnt <= n {
        //println!("start ra={:?}", ra);

        for i in 0..n {
            l[i].first = ra[i] ;
            l[i].second = if i + cnt < n {
                ra[i + cnt]
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
                nra[l[i].p] = i as isize;
            }
        }

        //println!("end ra={:?}", ra);
        swap(&mut ra, &mut nra);
        cnt <<= 1;
    }
    //return l
    //    .iter()
    //    .map(|e| e.p)
    //    .collect();

    // q: This should work as well, sould it not?
    // a: It looks like does but there has to be at 
    // least one iteration of the previous loop
    let mut res = vec![0; n];
    for (i, &r) in ra.iter().enumerate() {
        res[r as usize] = i;
    }
    return res;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    while let Some(line_res) = lines.next() {
        let line = line_res
            .unwrap()
            .chars()
            .collect::<Vec<char>>(); 
        let queries = lines
            .next()
            .unwrap()
            .unwrap();
        let suf_array = build(&line);
        
        let mut res = vec![];
        for (i, qis) in queries.split(" ").enumerate() {
            if i == 0 {
                continue
            } else {
                let qi = qis.parse::<usize>().unwrap();
                res.push(format!("{}", suf_array[qi]));
            }
        }
        println!("{}", res.join(" "));
    }

    Ok(())
}

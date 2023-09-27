use std::io::{self, BufRead, BufWriter, Write};
use std::cmp::{max, Ordering};
use std::mem::swap;
use std::char::from_digit;
use std::collections::{VecDeque, HashSet};

#[derive(Debug)]
struct MinQueue {
    min: VecDeque<usize>,
    que: VecDeque<usize>,
}

impl MinQueue {
    fn new() -> Self {
        Self {
            min: VecDeque::new(),
            que: VecDeque::new(),
        }
    }

    fn push(&mut self, n: usize) {
        self.que.push_back(n);
        while !self.min.is_empty() && n < *self.min.back().unwrap() {
            self.min.pop_back();
        }
        self.min.push_back(n);
    }

    fn pop(&mut self) -> usize {
        let n = self.que.pop_front().unwrap();
        if *self.min.front().unwrap() == n {
            self.min.pop_front();
        }
        return n;
    }

    fn min(&self) -> usize {
        return *self.min.front().unwrap();
    }
}

#[derive(Debug, Clone, Eq)]
struct Entry {
    fst: isize,
    snd: isize,
    p: usize,
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
        return (self.fst, self.snd) == (other.fst, other.snd);
    }
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

fn create_suffix_array(s: &Vec<usize>) -> Vec<usize> {
    let n = s.len();
    // just copy s
    let mut ra = s.clone();
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
            if l[i] == l[i - 1] {
                nra[l[i].p] = nra[l[i - 1].p];
            } else {
                nra[l[i].p] = i;
            }
        }

        k *= 2;
        swap(&mut ra, &mut nra);
    }
    return l
        .iter()
        .map(|e| e.p)
        .collect();
}

fn create_lcp_array(v: &Vec<usize>, sa: &Vec<usize>) -> Vec<usize> {
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

/* maybe to improve, create res with capacity */
fn merge_strings(v: &Vec<String>, capacity: usize) -> (Vec<usize>, Vec<usize>) {
    let mut groups = vec![0; capacity];
    let mut res = vec![0; capacity];
    let mut prev = 0;
    let mut k = 0;
    for (i, s) in v.iter().enumerate() {
        for c in s.chars() {
            let ord = c as usize;
            res[k] = ord + 200;
            //res.push(ord + 200); // poss more than 200 strings
            //groups.push(i);
            groups[k] = i;
            k += 1;
        }
        res[k] = i;
        groups[k] = i;
        k += 1;
    }
    return (res, groups);
}

fn format(v: &Vec<usize>) -> String {
    return v
        .iter()
        .map(|&u| if u < 200 {
            return '$'
        } else {
            return ((u - 200) as u8) as char;
        })
        .collect::<String>();
}

fn main() -> io::Result<()> {
    let stdout = io::stdout();
    let stdin = io::stdin();

    let mut lines = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;

    let mut lines_drain = lines.drain(..);

    let mut writer = BufWriter::with_capacity(64 * 1024, stdout);

    let mut first = true;

    loop {
        let n = lines_drain
            .next()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        if n == 0 {
            break;
        }

        if !first {
            writeln!(writer, "");
        }

        let mut strings = Vec::new();
        let mut capacity = 0;
        for _ in 0..n {
            let s = lines_drain.next().unwrap();
            capacity += s.len() + 1;
            strings.push(s);
        }

        let (merged, groups) = merge_strings(&strings, capacity);

        //let fmt = format(&merged);

        let sa = create_suffix_array(&merged);
        let lcp = create_lcp_array(&merged, &sa);


        /*println!("{:?}", lcp);
        println!("merged string: {}", fmt);
        for &i in &sa {
            println!("{}", &fmt[i..]);
        }*/

        let mut current = 0;
        let treshold = (strings.len() >> 1) + 1;
        let mut cnt = vec![0; strings.len()];
        let mut l = strings.len();
        let mut mx = 0;
        let mut res_pairs = Vec::new();

        let mut q = MinQueue::new();

        // do sliding window
        for r in strings.len()..sa.len() {

            while l < r && current >= treshold {
                q.pop();
                if q.min() > mx {
                    mx = q.min();
                    res_pairs.clear();
                    res_pairs.push((sa[l], sa[l] + q.min()));
                } else if q.min() == mx && mx != 0{
                    res_pairs.push((sa[l], sa[l] + q.min()));
                }
                let g = groups[sa[l]];
                cnt[g] -= 1;
                if cnt[g] == 0 {
                    current -= 1;
                }
                l += 1;
            }
            
            let g = groups[sa[r]];
            cnt[g] += 1;
            if cnt[g] == 1 {
                current += 1;
            }
            q.push(lcp[r]);
        }

        let mut last = "".to_string();
        let mut res = "".to_string();


        if mx == 0 {
            writeln!(writer, "?");
        } else {  
            /* suffix array guarantees sorted order!*/
            for (s, e) in res_pairs {
                res = merged[s..e]
                    .iter()
                    .map(|&u| ((u - 200) as u8) as char)
                    .collect::<String>();
                if res != last {
                    writeln!(writer, "{}", res);
                    last = res;
                }
            }
        }
        first = false;
    }

    Ok(())
}

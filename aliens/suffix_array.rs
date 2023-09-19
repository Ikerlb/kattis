use std::io::{BufRead, self};
use std::cmp::{Ordering, max, min};
use std::mem::swap;
use std::collections::VecDeque;

struct MinQueue {
    q: VecDeque<usize>,
    mq: VecDeque<usize>,
}

impl MinQueue {
    fn new() -> Self {
        return Self {
            q: VecDeque::new(),
            mq: VecDeque::new()
        }
    }

    fn pop(&mut self) -> usize {
        let ret = self.q.pop_front().unwrap(); 
        if ret == *self.mq.front().unwrap() {
            self.mq.pop_front();
        }
        return ret;
    }

    fn push(&mut self, a: usize) {
        self.q.push_back(a);
        while let Some(&last) = self.mq.back(){
            if a < last {
                self.mq.pop_back();
            } else {
                break;
            }
        }
        self.mq.push_back(a);
    }

    fn min(&self) -> usize {
        return *self.mq.front().unwrap();
    }
}

struct MinDeque {
    q: VecDeque<usize> 
}



struct SegmentTree {
    arr: Vec<usize>,
    tree: Vec<usize>,
}

impl SegmentTree {
    fn new(arr: Vec<usize>) -> Self {
        let n = arr.len();
        let mut st = Self {
            arr: arr,
            tree: vec![0; n * 4]
        };
        st.build(1, 0, n - 1);    
        return st;
    }

    fn build(&mut self, i: usize, l: usize, r: usize) -> usize {
        if l == r {
            self.tree[i] = self.arr[l];
            return self.arr[l];
        } else {
            let mid = (l + r) >> 1;
            let left  = self.build(i * 2, l, mid); 
            let right = self.build(i * 2 + 1, mid + 1, r);
            self.tree[i] = max(left, right);
            return self.tree[i]
        }
    }

    fn query(&self, l: usize, r: usize) -> usize {
        return self.query_range(1, 0, self.arr.len() - 1, l, r);
    }

    fn query_range(&self, i: usize, tl: usize, tr: usize, l: usize, r: usize) -> usize{
        if l > r {
            return 0;
        } else if l == tl && r == tr {
            return self.tree[i];
        } else {
            let tm = (tl + tr) >> 1;
            let left = self.query_range(2*i, tl, tm, l, min(r, tm));
            let right = self.query_range(2*i+1, tm + 1, tr, max(l, tm + 1), r);
            return max(left, right);
        }
    }
}

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

fn format(t: &Vec<char>, sa: &Vec<usize>, lcp: &Vec<usize>) {
    // first natural ordering
    let n = t.len();
    // get sa index
    let mut in_sa = vec![0; n];
    for i in 0..n {
        in_sa[sa[i]] = i;
    }

    let npad = format!("{}", n - 1).len();
    let lcp_pad = format!("{}", lcp.iter().max().unwrap()).len();
    let first = (0..n)
        .map(|i| {
            let s = t[i..].iter().collect::<String>();
            let idx = format!("{:>width$}", i, width = npad);
            let s2 = format!("{:>width$}", lcp[in_sa[i]], width = lcp_pad);
            return format!("{} {:>width$} {}", idx, s, s2, width = n);
        })
        .collect::<Vec<String>>();
    let snd = sa
        .iter()
        .enumerate()
        .map(|(i, &si)| {
            let s = t[si..].iter().collect::<String>();
            let idx = format!("{:>width$}", si, width = npad);
            let s2 = format!("{:>width$}", lcp[i], width = lcp_pad);
            return format!("{} {:>width$} {}", idx, s, s2, width = n);

        })
        .collect::<Vec<String>>();
    println!("{}\n", first.join("\n"));
    println!("{}", snd.join("\n"));
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

    while k <= n {
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

// caca -> 0
// aca  -> 1
// ca   -> 2
// a    -> 3

// a    -> 3
// aca  -> 1
// ca   -> 2
// caca -> 0

// phi[0] is the pred of caca in sorted order which is 2
// phi[1] is the pred of aca in sorted order which is 3
// phi[2] is the pred of ca in sorted order which is 1
// phi[3] is the pred of a in sorted order which is -1

/*
 * t is the string dumped to a vec
 * sa is the sorted suffix array
 * */ 
fn build_lcp_array(t: &Vec<char>, sa: &Vec<usize>) -> Vec<usize> {
    // build phi
    let n = t.len();
    let mut phi = vec![-1; n];
    for i in 1..n {
        phi[sa[i]] = sa[i - 1] as isize; 
    }

    let mut l = 0;
    let mut plcp = vec![0; n];
    for i in 0..n {
        if phi[i] == -1 {
            continue;
        }
        let mut p = phi[i] as usize;
        while i + l < n && p + l < n && t[i + l] == t[p + l] {
            l += 1;
        }
        plcp[i] = l;
        if l != 0 {
            l -= 1;
        }
    }
    let mut lcp = vec![0; n];
    for i in 0..n {
        lcp[i] = plcp[sa[i]];
    }
    return lcp;
}

fn solve(sa: &Vec<usize>, m: usize) -> String {
    return "".to_string();
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
        let lcp = build_lcp_array(&v, &sa);

        let mut ln = (0, 0);

        if m == 1 {
            ln = (v.len(), 0);
        } else {
            let st = SegmentTree::new(sa);
            let mut minq = MinQueue::new();

            /* omit first entry */
            for i in 1..m {
                minq.push(lcp[i]);
            }

            ln = (minq.min(), st.query(0, m - 1));

            for i in m..lcp.len() {
                minq.pop();
                minq.push(lcp[i]); 
                if minq.min() > ln.0 {
                    ln = (minq.min(), st.query(i - m + 1, i));
                } else if minq.min() == ln.0 && st.query(i - m + 1, i) > ln.1 {
                    ln = (minq.min(), st.query(i - m + 1, i));
                }
            }
        }


        if ln.0 != 0 {
            println!("{} {}", ln.0, ln.1);
        } else {
            println!("none");
        }
    }


    Ok(())
}

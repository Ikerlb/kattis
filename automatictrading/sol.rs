use std::io::{self, BufRead};
use std::cmp::Ordering;
use std::mem::swap;
use std::cmp::{max, min};

#[derive(Clone, Eq)]
struct Entry {
    first: isize,
    second: isize,
    p: usize,
}

impl Entry {
    fn new(first: isize, second: isize, p: usize) -> Self {
        Entry {
            first: first,
            second: second,
            p: p,
        }
    }
}

impl Ord for Entry {
    fn cmp(&self, other: &Self) -> Ordering {
        (self.first, self.second).cmp(&(other.first, other.second))
    }
}

impl PartialOrd for Entry {
    fn partial_cmp(&self, other: &Self) -> Option<Ordering> {
        Some(self.cmp(other))
    }
}

impl PartialEq for Entry {
    fn eq(&self, other: &Self) -> bool {
        self.first == other.first && self.second == other.second
    }
} 

struct SegmentTree<'a> {
    tree: Vec<usize>,
    arr: &'a Vec<usize>,    
}

impl<'a> SegmentTree<'a> {
    fn new(arr: &'a Vec<usize>) -> Self {
        let mut st = Self{
            arr: arr,
            tree: vec![std::usize::MAX; 4 * arr.len()], 
        };

        st.build(0, arr.len() - 1, 1);

        return st;
    }

    fn build(&mut self, al: usize, ar: usize, i: usize) -> usize {
        if al == ar {
            self.tree[i] = self.arr[al];
            return self.arr[al];
        } else {
            let mid = (al + ar) >> 1;
            let left = self.build(al, mid, 2 * i);
            let right = self.build(mid + 1, ar, 2 * i + 1);
            self.tree[i] = min(left, right);
            return self.tree[i];
        }
    }

    pub fn query(&self, l: usize, r: usize) -> usize {
        return self.query_range(1, 0, self.arr.len() - 1, l, r);
    }

    fn query_range(&self, i: usize, tl: usize, tr: usize, l: usize, r: usize) -> usize{
        if l > r {
            return std::usize::MAX;
        } else if l == tl && r == tr {
            return self.tree[i];
        } else {
            let tm = (tl + tr) >> 1;
            let left = self.query_range(2*i, tl, tm, l, min(r, tm));
            let right = self.query_range(2*i+1, tm + 1, tr, max(l, tm + 1), r);
            return min(left, right);
        }
    }
}

fn build_suffix_array(s: &Vec<char>) -> Vec<usize> {
    let n = s.len();
    let mut ra = s 
        .iter()
        .map(|&n| n as isize)
        .collect::<Vec<isize>>();
    let mut nra = vec![0; n];
    let mut l = vec![Entry::new(0, 0, 0); n];

    let mut k = 1;
    while k < n {
        for i in 0..n {
            l[i].first = ra[i];
            l[i].second =  if i + k < n {
                ra[i + k]
            } else {
                -1
            };
            l[i].p = i;
            nra[i] = 0;
        }

        l.sort();

        nra[0] = 0;
        for i in 1..n {
            if l[i] == l[i - 1] {
                nra[l[i].p] = nra[l[i - 1].p];
            } else {
                nra[l[i].p] = i as isize;
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

fn format(s: &Vec<char>, sa: &Vec<usize>) -> String {
    let mut res = Vec::new();
    for i in sa {
        let ss = s[*i..].iter().collect::<String>();
        res.push(format!("{} -> {}", i, ss));
    }
    return res.join("\n");
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let lines = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;
    let s = &lines[0]
        .chars()
        .collect::<Vec<_>>();

    let sa = build_suffix_array(&s);
    //println!("sa: {:?}", sa);
    let mut isa = vec![0; sa.len()];
    for i in 0..sa.len() {
        isa[sa[i]] = i;
    }
    //println!("isa: {:?}", isa);
    //println!("sa order:\n{}", format(&s, &sa));
    let lcpa = build_lcp_array(&s, &sa); 
    //println!("lcpa: {:?}", lcpa);
    let st = SegmentTree::new(&lcpa);


    for qs in &lines[2..] {
        let mut split = qs
            .split(" ")
            .map(|ns| ns.parse::<usize>().unwrap());
        let l = split.next().unwrap();
        let r = split.next().unwrap();

        let mut li = isa[l];
        let mut ri = isa[r];

        if li > ri {
            swap(&mut li, &mut ri)
        }

        //println!("li: {} ri: {}", li + 1, ri);
        let q = st.query(li + 1, ri); 
        println!("{}", q);
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use SegmentTree;

    #[test]
    fn test_segment_tree() {
        let n = 10;
        let v = (0..n).collect::<Vec<_>>();
        let st = SegmentTree::new(&v);
        for l in 0..n {
            for r in l..n {
                let q = st.query(l, r);
                let ans = v[l..=r]
                    .iter()
                    .map(|&i| i)
                    .min()
                    .unwrap();
                assert!(q == ans, format!("l: {} r: {}, q is {}, should be {}", l, r, q, ans));
            }
        }
    }
}

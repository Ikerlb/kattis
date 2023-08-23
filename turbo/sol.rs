use std::io::{self, BufRead, BufWriter, Write};

struct FenwickTree {
    t: Vec<isize>,
}

impl FenwickTree {
    fn new(n: usize) -> Self {
        return Self {
            t: vec![0; n + 1]
        };
    }

    fn add(&mut self, mut i: usize, delta: isize) {
        i += 1;
        while i < self.t.len() {
            self.t[i] += delta;
            i += i & (0 - i);
        }
    }

    /* yields result of 0..=i */
    fn sum(&mut self, mut i: usize) -> isize {
        i += 1; 
        let mut s = 0;
        while i > 0 {
            s += self.t[i];
            i -= i & (0 - i);
        }
        return s;
    }

    fn sum_range(&mut self, l: usize, r: usize) -> isize {
        if l == 0 {
            return self.sum(r);
        } else {
            return self.sum(r) - self.sum(l - 1);
        }
    }
}

// 5,4,3,7,1,2,6
// 1,1,1,1,1,1,1
// 1,1,1,1,0,1,1
// 1,1,1,0,0,1,1
// 1,1,1,0,0,0,1
// 1,1,1,0,0,0,0
// 1,1,0,0,0,0,0
// 0,1,0,0,0,0,0
// 0,0,0,0,0,0,0
//

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut writer = BufWriter::new(stdout.lock());
    let arr = stdin
        .lock()
        .lines()
        .map(|res| res.unwrap().parse::<usize>().unwrap())
        .collect::<Vec<usize>>();

    let n = arr[0];

    let mut ft = FenwickTree::new(n);
    for i in 0..n {
        ft.add(i, 1);
    }
    let mut pos = vec![0; n];
    for (i, &n) in arr[1..].iter().enumerate() {
        pos[n - 1] = i;
    }

    let mut l = 0;
    let mut r = n - 1;
    let mut turn = 0;
    while l <= r {
        if turn == 0 {
            ft.add(pos[l], -1);
            let res = ft.sum_range(0, pos[l]);
            writeln!(writer, "{}", res);
            l += 1;
        } else {
            ft.add(pos[r], -1);
            let res = ft.sum_range(pos[r], n - 1);
            writeln!(writer, "{}", res);
            r -= 1;
        }
        turn = 1 - turn;
    }

    Ok(())
}

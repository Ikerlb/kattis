use std::io::{self, BufRead, BufWriter, Write};
use std::collections::HashMap;
use std::cmp::{max, min};

struct SegmentTree<'a> {
    t: Vec<isize>,
    arr: &'a Vec<isize>,
}

impl<'a> SegmentTree<'a> {
    fn build(&mut self, l: usize, r: usize, ti: usize) -> isize {
        if l == r {
            self.t[ti] = self.arr[l];
            return self.t[ti];
        } else {
            let mid = (l + r) >> 1;
            let lchild = self.build(l, mid, ti << 1);
            let rchild = self.build(mid + 1, r, (ti << 1) + 1);
            self.t[ti] = max(lchild, rchild);
            return self.t[ti];
        }
    }

    fn query_handler(&self, l: usize, r: usize, i: usize, j: usize, ti: usize ) -> isize {
        if i > j {
            return isize::MIN;
        } else if l >= i && r <= j {
            return self.t[ti];
        } else {
            let mid = (l + r) >> 1;
            let left = self.query_handler(l, mid, i, min(mid, j), ti * 2);
            let right = self.query_handler(mid + 1, r, max(mid + 1, i), j, (ti * 2) + 1);
            return max(left, right);
        }
    }

    fn query(&self, l: usize, r: usize) -> isize {
        return self.query_handler(0, self.arr.len() - 1, l, r, 1);
    }

    fn new(arr: &'a Vec<isize>) -> Self {
        let n = arr.len();
        let tree = vec![isize::MIN; 4 * arr.len()];
        let mut st = Self {
            t: tree,        
            arr: arr,
        };

        st.build(0, n - 1, 1);

        return st;
    }
}

fn first_greater_or_equal(a: &Vec<isize>, target: isize) -> usize{
    let mut l = 0isize;
    let mut r = (a.len() - 1) as isize;

	while (l < r) {
		let m = (l + r) >> 1;
		if a[m as usize] < target {
            l = m + 1;
        } else {
            r = m;
        }
	}
	return l as usize;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();

    let mut lines = stdin
        .lock()
        .lines()
        .map(|res| res.unwrap());

    let mut first = true; 
    loop {

        let n = lines.next().unwrap().parse::<usize>().unwrap();
        let mut arr = Vec::new();
        let mut keys = Vec::new();
        for _ in 0..n {
            let binding = lines
                .next()
                .unwrap();
            let mut entry = binding
                .split(" ")
                .map(|s| s.parse::<isize>().unwrap());
            let year = entry.next().unwrap();
            let amnt = entry.next().unwrap();
            keys.push(year);
            arr.push(amnt);
        }


        let qs = lines.next().unwrap().parse::<usize>().unwrap();

        if n == 0 && qs == 0 {
            break;
        }

        if first {
            first = false;
        } else {
            println!();
        }

        //println!("keys: {:?}", keys);
        //println!("vals: {:?}", arr);

        let st = SegmentTree::new(&arr);

        for _ in 0..qs {
            let binding = lines
                .next()
                .unwrap();
            let mut entry = binding
                .split(" ")
                .map(|s| s.parse::<isize>().unwrap());

            let y = entry.next().unwrap();
            let x = entry.next().unwrap();

            //println!("{} {}", x, y);

            if (keys[0] >= x || keys[keys.len()-1] <= y) {
				println!("maybe");
				continue;
			}

            let mut xp = first_greater_or_equal(&keys, x);
            let mut yp = first_greater_or_equal(&keys, y);

            if keys[xp] > x {
                xp -= 1;
            }

            if yp >= xp {
                println!("maybe");
                continue;
            }

            if !(keys[yp] != y || keys[xp] != x || arr[yp] >= arr[xp]) {
                println!("false");
                continue;
            }

            let lq = if keys[yp] == y {
                yp + 1
            } else {
                yp
            };

            let rq = if keys[xp] == x {
                xp - 1
            } else {
                xp
            };

            let mx = if yp <= xp {
                st.query(lq, rq)
            } else {
                0
            };

            if keys[xp] == x && arr[xp] <= mx {
                println!("false");
                continue;
            }

            if keys[yp] == y && arr[yp] <= mx {
                println!("false");
                continue;
            }

            if keys[xp] == x && keys[yp] == y && (xp - yp) as isize == (x - y) {
				println!("true");
			} else {
				println!("maybe");
			}
            
        }


        //let mut hm = HashMap::new();
        lines.next();
        //|let mut ft = ;
    }

    Ok(())
}

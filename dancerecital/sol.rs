use std::io::{self, BufRead, Error};

fn to_counter(s: &str) -> [isize; 26] {
    let mut res = [0; 26];
    for c in s.chars() {
        let i = (c as usize - 'A' as usize);
        res[i] += 1
    }
    res
}

fn permutations<T, F>(arr: &mut [T], f: &mut F) -> ()
where
    F: FnMut(&mut [T]),
{
    perm(arr, f, 0);
}

fn perm<T, F>(arr: &mut [T], f: &mut F, i: usize)
where 
    F: FnMut(&mut [T]),
{
    if i > arr.len() {
        f(arr);
        return 
    }
    perm(arr, f, i + 1);
    for j in i + 1..arr.len() {
        arr.swap(i, j);
        perm(arr, f, i + 1);
        arr.swap(i, j);
    }
}

fn main() {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_line(&mut buffer);

    let n = buffer.trim().parse::<i64>().unwrap();

    let mut routines: Vec<[isize; 26]> = Vec::new();
    
    for i in 0..n {
        let mut b = String::new();
        handle.read_line(&mut b);

        let idfk = b.trim();

        routines.push(to_counter(&idfk));
    }

    let mut m = 10000;
    permutations(&mut routines, &mut |arr| {
        let mut res = 0;
        for i in 0..(arr.len() - 1) {
            for j in 0..arr[i].len() {
                if arr[i][j] > 0 && arr[i + 1][j] > 0 {
                    res += 1        
                }
            }
        }
        if res < m {
            m = res;
        }
    });
    println!("{}", m);
}

use std::io::{self, BufRead};

fn prod(a: u32, b: u32, m: u32) -> u32 {
    let p = a as u64 * b as u64;
    return (p % m as u64) as u32;
}

fn pow(a: u32, b: u32, m: u32) -> u32 {
    if b == 0 {
        return 1;
    } else if b & 1 == 0 {
        let half = pow(a, b >> 1, m);
        return prod(half, half, m)
    } else {
        let half = pow(a, b >> 1, m);
        return prod(a, prod(half, half, m), m);
    }
}

/* p should be bigger than 2 */
fn inverse(a: u32, p: u32) -> u32 {
    return pow(a, p - 2, p);
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    let MAXN = 100001;
    let p: u32 = 1000000007;

    let mut catalan = vec![1; MAXN];

    for i in 0..(MAXN - 1) {
        let iu32 = i as u32;
        let fst = (4 * iu32 + 2) % p;
        let snd = catalan[i];
        let thd = inverse(iu32 + 2, p);
        catalan[i + 1] = prod(fst, prod(snd, thd, p), p);
    }

    let n = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    println!("{}", catalan[n]);

    return Ok(());
}

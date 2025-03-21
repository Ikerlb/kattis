use std::io::{self, BufRead};

fn sieve(upto: u64) -> Vec<bool> {
    let uptou = upto as usize;
    let mut res = vec![true; uptou + 1];
    res[0] = false;
    res[1] = false;

    let sqrt = (upto as f64).sqrt() as usize; 
    for i in 2..=sqrt {
        if res[i] {
            for j in ((i * i)..=uptou).step_by(i) {
                res[j] = false;
            }
        }
    }
    return res;
}

fn is_prime(n: u64) -> bool {
    let limit = (n as f64).sqrt() as u64;

    for i in 2..=limit {
        if n % i == 0 {
            return false;
        }
    }

    true
}

fn solve(mut n: u64) -> Option<(u64, u64, u64)> {
    n = n - 3;
    for fst in 2..=n {
        let ufst = fst as u64; 
        let snd = n - ufst;
        if is_prime(ufst) && is_prime(snd) {
            return Some((3, ufst, snd));
        }
    }
    return None;
}

/*
 * "All odd numbers greater
 * than  can be written as
 * the sum of three primes"
 * well this is obvious isn't
 * it? lets take number 3
 * if we take Goldbach's first
 * conjecture for granted (1M
 * bucks for me right here) and we have n
 * as input, n is odd and n > 5
 * then we need to know if n - 3
 * (an even number) can be written
 * as the sum of two primes (Goldbach's!)
 */
fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|line_res| line_res.unwrap());
    let n = lines
        .next()
        .unwrap()
        .parse::<u64>()
        .unwrap();

    //println!("n is {}", n);

    //let s = sieve(10u64.pow(8));
    //let primes: Vec<_> = (0..s.len())
    //    .filter(|&i| s[i])
    //    .collect();

    if let Some((fst, snd, thd)) = solve(n) {
        assert!(fst + snd + thd == n); 
        println!("{} {} {}", fst, snd, thd);
    } else {
        println!("Neibb");
    }

    Ok(())
}

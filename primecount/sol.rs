use std::io::{self, BufRead};
use std::collections::BTreeMap;

fn primes_upto(upto: usize) -> Vec<i64> {
    let mut primes = Vec::new();
    let mut v = vec![true; upto + 1];
    v[0] = false;
    v[1] = false;
    for i in 2..(upto + 1) {
        if v[i] == false {
            continue;
        }
        primes.push(i as i64);
        for j in ((i * i)..=upto).step_by(i) {
            v[j] = false;
        }
    }
    return primes;
}

fn phi(x: i64, a: i64, p: &[i64]) -> i64 {
    if a == 0 {
        return x;
    } else if a == 1 {
        return x - (x >> 1);
    }
    let amm = a - 1;
    let pa = p[amm as usize];
    if x <= pa {
        return 1;
    }

    return phi(x, amm, p) - phi(x / pa, amm, p);
}

fn count_primes(n: i64, p: &[i64]) -> i64 {
    if n < 2 {
        return 0;
    }

    let a = count_primes((n as f64).sqrt() as i64, p);
    return phi(n, a, p) + a - 1;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();

    let input = stdin
        .lock()
        .lines()
        .collect::<io::Result<String>>()?;

    let n = input.parse::<i64>().unwrap();

    let n_sqrt = (n as f64).sqrt() as usize;

    let primes = primes_upto(n_sqrt + 10); 

    println!("{}", count_primes(n, &primes[..]));

    return Ok(());
}

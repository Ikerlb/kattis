use std::io::{self, BufRead};
use std::collections::HashMap;

fn sieve(upto: usize) -> Vec<usize> {
    let mut is_prime = vec![true; upto + 1];
    is_prime[0] = false;
    is_prime[1] = false;
    for i in 2..upto {
        for j in ((i * i)..=upto).step_by(i) {
            is_prime[j] = false;
        }
    }
    return (2..=upto).filter(|&i| is_prime[i]).collect();
}

fn main() -> io::Result<()> {
    let primes = sieve(35000);
    let primes_set = primes
        .iter()
        .enumerate()
        .map(|(i, &p)| (p, i))
        .collect::<HashMap<usize, usize>>();

    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap().parse::<usize>().unwrap());
    let tcs = lines.next().unwrap();

    for tc in 0..tcs {
        let n = lines.next().unwrap();
        let mut sum_of_primes = Vec::new();
        for (i, &p) in primes.iter().enumerate() {
            if p >= n {
                break;
            }
            let other = n - p;
            if let Some(&idx) = primes_set.get(&other) {
                if idx >= i {
                    sum_of_primes.push((p, other));
                }
            }
        }
        println!("{} has {} representation(s)", n, sum_of_primes.len());
        for (p1, p2) in sum_of_primes {
            println!("{}+{}", p1, p2);
        }
        println!();
    }

    Ok(())
}

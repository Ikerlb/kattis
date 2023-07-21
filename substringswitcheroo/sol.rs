use std::io::{BufRead, self};
use std::collections::HashSet;

fn count(a: &[usize]) -> [usize; 26] {
    let mut res: [usize; 26] = [0; 26];
    for &i in a {
        res[i] += 1;
    }
    return res;
}

/*fn pow(a: usize, b: usize, p: usize) -> usize {
    if b == 0 {
        return 1;
    }
    let half = pow(a, b >> 1, p);
    if b & 1 == 1 {
        return (((half * half) % p) * a) % p;
    } else {
        return (half * half) % p;
    }
}*/

fn pow(a: usize, b: usize, p: usize) -> usize {
    if b == 0 {
        return 1;
    }
    let half = pow(a, b >> 1, p);
    if b & 1 == 1 {
        return mod_mult(mod_mult(half, half, p), a, p);
    } else {
        return mod_mult(half, half, p);
    }
}

fn num(c: char) -> usize {
    return c as usize - 'a' as usize;
}

fn hash(a: &[usize], bases: &Vec<usize>, p: usize) -> usize {
    return count(a)
        .iter()
        .enumerate()
        .map(|(i, &f)| pow(bases[i], f, p))
        .fold(1, |acc, e| mod_mult(acc, e, p));
}

fn to_string(a: &[usize]) -> String {
    return a
        .iter()
        .map(|&x| char::from_u32((x + ('a' as usize)) as u32).unwrap())
        .collect::<String>();
}

/* 
 * could just mash into a single integer but 
 * this generalizes better, albeit slower.
 * */
fn merge(hashes: &Vec<usize>) -> String {
    return hashes
        .iter()
        .map(|h| format!("{}", h))
        .collect::<Vec<_>>()
        .join(",");
}

fn mod_mult(a: usize, b: usize, m: usize) -> usize {
    return ((a as u128 * b as u128) % (m as u128)) as usize;
}

fn has_anagramic_substrings(a: &Vec<usize>, b: &Vec<usize>, bases: &Vec<usize>, inverses: &Vec<Vec<usize>>, ps: &Vec<usize>, k: usize) -> Option<usize> {
    let mut cbs = HashSet::new();

    let mut hbs = ps
        .iter()
        .map(|&p| hash(&b[..k], bases, p))
        .collect::<Vec<_>>();
    cbs.insert(merge(&hbs)); 
    for i in k..b.len() {
        for j in 0..ps.len() {
            hbs[j] = mod_mult(hbs[j], inverses[j][b[i - k]], ps[j]);
            hbs[j] = mod_mult(hbs[j], bases[b[i]], ps[j]);
        }
        cbs.insert(merge(&hbs));
    }

    let mut has = ps 
        .iter()
        .map(|&p| hash(&a[..k], bases, p))
        .collect::<Vec<_>>();
        
    if cbs.contains(&merge(&has)) {
        return Some(0);
    }
    for i in k..a.len() {
        for j in 0..ps.len() {
            has[j] = mod_mult(has[j], inverses[j][a[i - k]], ps[j]);
            has[j] = mod_mult(has[j], bases[a[i]], ps[j]);
        }
        if cbs.contains(&merge(&has)) {
            return Some(i - k + 1);
        }
    }

    return None;
}

fn solve(s1: &Vec<usize>, s2: &Vec<usize>, bases: &Vec<usize>, inverses: &Vec<Vec<usize>>, p: &Vec<usize>) -> String {
    for k in (1..=s1.len()).rev() {
        if let Some(i) = has_anagramic_substrings(s1, s2, bases, inverses, p, k) {
            return s1[i..i + k]
                .iter()
                .map(|j| char::from_u32((j + ('a' as usize)) as u32).unwrap())
                .collect::<String>();
        }
    }
    return "NONE".to_string();
}

/*
 * Fermat's little theorem:
 * a^(p - 1) % p == 1
 * which means that since a*(a^(p - 2)) == 1 
 * a^(p-2) is a modulo inverse of a
 */
fn create_inverses(bases: &Vec<usize>, modulo: usize) -> Vec<usize> {
    return bases
        .iter()
        .map(|&b| pow(b, modulo - 2, modulo))
        .collect::<Vec<usize>>();
}

fn main() -> io::Result<()> {
    let mut lines = io::stdin()
        .lock()
        .lines();
    let tcs = lines.next().unwrap().unwrap().parse::<usize>().unwrap();


    // my program definitely had overflowing bugs
    // would now need a little more consistency on 
    // the concrete types (usize could be u32 or u64)
    // this would work ok (that would be u64)
    // as anything over u128 would simply overflow on some 
    // multiplications, even if the modulo keeps it within 
    // bounds, TODO: try with experimental widening_mult!
    // kinda miss python amirite?
    let modulos = vec![614244627451450103]; 
    let bases = vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101];
    let inverses = &modulos
        .iter()
        .map(|&modulo| create_inverses(&bases, modulo))
        .collect::<Vec<_>>();
    for _ in 0..tcs {
        // ugh much better to just collect the lines
        let s1 = lines
            .next()
            .unwrap()
            .unwrap()
            .chars()
            .map(|c| num(c))
            .collect::<Vec<usize>>();

        let s2 = lines
            .next()
            .unwrap()
            .unwrap()
            .chars()
            .map(|c| num(c))
            .collect::<Vec<usize>>();
        println!("{}", solve(&s1, &s2, &bases, &inverses, &modulos));        
    }

    Ok(())
}

use std::collections::HashSet;
use std::io::{BufRead, self};

#[derive(Clone, Debug)]
enum Token {
    OpenPar,
    ClosedPar,
    Comma,
    Number(usize),
}

fn tokenize(s: String) -> Vec<Token> {
    let mut v = Vec::new();
    let mut cur = 0;
    for c in s.chars() {
        if c == '(' {
            v.push(Token::OpenPar);
        } else if c == ')' {
            if cur != 0 {
                v.push(Token::Number(cur));
                cur = 0;
            }
            v.push(Token::ClosedPar);
        } else if c == ',' {
            if cur != 0 {
                v.push(Token::Number(cur));
                cur = 0;
            }
            v.push(Token::Comma);
        } else {
            cur = 10 * cur;
            cur += c.to_digit(10).unwrap() as usize;
        }
    }
    return v;
}

// ((3,(1,(5,2))),4)
fn dfs(s: String, bases: &Vec<u64>, m: u64) -> HashSet<u64> {
    let mut toks = tokenize(s); 
    let mut s = vec![0];
    let mut set: HashSet<u64> = HashSet::new();
    for c in toks {
        match c {
            Token::OpenPar => {
                s.push(0);
            }, 
            Token::ClosedPar => {
                let ret = s.pop().unwrap();
                set.insert(ret);
                let mut last = s.last_mut().unwrap();
                *last = (*last + ret) % m;
            },
            Token::Comma => {
                continue;
            },
            Token::Number(n) => {
                set.insert(bases[n]);
                let mut last = s.last_mut().unwrap();
                *last = (*last + bases[n]) % m;
            }
        }
    }
    return set;
}

fn prod(a: u64, b: u64, m: u64) -> u64 {
    let p = a as u128 * b as u128; 
    return (p % m as u128) as u64
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let n = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    let alice = lines
        .next()
        .unwrap()
        .unwrap();

    let bobby = lines
        .next()
        .unwrap()
        .unwrap();

    let b = 131;
    let m = 614889782588491410;

    let mut bases = vec![1; n + 1];
    for i in 1..n {
        bases[i] = prod(b, bases[i - 1], m);
    }

    let s1 = dfs(alice, &bases, m);
    let s2 = dfs(bobby, &bases, m);

    let inter = s1
        .intersection(&s2)
        .collect::<Vec<_>>();

    println!("{}", inter.len());

    Ok(())
}

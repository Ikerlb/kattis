use std::io::{self, BufRead};

fn solve(n: usize, a: usize, b: usize, c: usize, x: usize, y: usize) -> usize {

    let mut v = vec![0; n];
    v[0] = a;

    for i in 1..n {
        v[i] = ((v[i - 1] * b) + a) % c;
    }
    
    v.sort();

    let mut res = 0;
    for ri in v {
        res = ((res * x) + ri) % y;
    }
    res
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let lines = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<String>>>()?;

    let mut iter = lines.iter();

    let tcs = iter
        .next()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    for _ in 0..tcs {
        let n = iter 
            .next()
            .unwrap()
            .parse::<usize>()
            .unwrap();

        let mut abc = iter 
            .next()
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse::<usize>().unwrap());
        let a = abc.next().unwrap();
        let b = abc.next().unwrap();
        let c = abc.next().unwrap();
    
        let mut xy = iter 
            .next()
            .unwrap()
            .split_whitespace()
            .map(|x| x.parse::<usize>().unwrap());
        let x = xy.next().unwrap();
        let y = xy.next().unwrap();

        //println!("n={}", n);
        //println!("a={} b={} c={}", a, b, c);
        //println!("x={} y={}", x, y);

        println!("{}", solve(n, a, b, c, x, y));

    }

    Ok(())
}

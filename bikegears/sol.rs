use std::io::{self, BufRead, BufWriter};

struct Gear {
    front: usize,
    back: usize,
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|line_res| line_res.unwrap());
    let first_handler = lines
        .next()
        .unwrap();
    let mut first = first_handler
        .split(" ")
        .map(|s| s.parse::<usize>().unwrap());
    let f = first.next().unwrap();
    let b = first.next().unwrap();

    let mut v: Vec<Gear> = Vec::with_capacity(f * b);
    
    let front = lines
        .next()
        .unwrap()
        .split(" ")
        .map(|ns| ns.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    let back = lines
        .next()
        .unwrap()
        .split(" ")
        .map(|ns| ns.parse::<usize>().unwrap())
        .collect::<Vec<_>>();

    for &f_g in &front {
        for &b_g in &back {
            v.push(Gear {
                front: f_g,
                back: b_g 
            });
        }
    }

    v.sort_by(|a, b| {
        let a_tup = (a.front as f128 / a.back as f64, a.front);
        let b_tup = (b.front as f128 / a.back as f64, a.front); 
        return a_tup
            .partial_cmp(&b_tup)
            .unwrap();
    });

    for g in v {
        //println!("({},{}) {}", g.front, g.back, g.front as f64 / g.back as f64);
        println!("({},{})", g.front, g.back);
    }

    Ok(())
}

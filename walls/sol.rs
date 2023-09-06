use std::io::{BufRead, self};
use std::collections::HashSet;

#[derive(Debug, Clone)]
struct Point {
    x: isize,
    y: isize,
}

impl Point {
    fn new(x: isize, y: isize) -> Self {
        return Self {
            x: x,
            y: y,
        };
    }
}

struct Circle {
    center: Point,
    radius: isize,
}

impl Circle {
    fn new(p: Point, r: isize) -> Self {
        Self {
            center: p,
            radius: r,
        }
    }

    fn contains(&self, p: &Point) -> bool {
        let x = p.x - self.center.x;
        let y = p.y - self.center.y;
        let r = self.radius;
        return x * x + y * y <= r * r;
    }
}

fn combs(v: &[usize], k: usize) -> Vec<Vec<usize>> {
    if k == 0 {
        return vec![Vec::new()];
    }
    if v.len() == 0 {
        return Vec::new();
    }

    let mut fst = combs(&v[1..], k - 1);
    for c in &mut fst {
        c.push(v[0]);
    }
    let mut snd = combs(&v[1..], k);
    fst.append(&mut snd);
    return fst;
}

fn solve(matches: &Vec<HashSet<(isize, isize)>>, mids: &Vec<Point>, k: usize) -> bool {
    let v = (0..matches.len()).collect::<Vec<usize>>();
    // we want  
    return false;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    let handler = lines
        .next()
        .unwrap()
        .unwrap();
    let mut first = handler
        .split(" ")
        .map(|s| s.parse::<isize>().unwrap());

    let l = first.next().unwrap();    
    let w = first.next().unwrap();    
    let n = first.next().unwrap();    
    let r = first.next().unwrap();    

    let middles = vec![
        Point::new(-l/2, 0),
        Point::new(l/2, 0),
        Point::new(0, -w/2),
        Point::new(0, w/2)
    ];

    let mut matches = vec![HashSet::new(); middles.len()];

    for line_res in lines {
        let line = line_res.unwrap();
        let mut split = line
            .split(" ")
            .map(|s| s.parse::<isize>().unwrap());

        let x = split.next().unwrap();
        let y = split.next().unwrap();
        let p = Point::new(x, y);
        let c = Circle::new(p.clone(), r);

        for (i, middle) in middles.iter().enumerate() {
            if c.contains(middle) {
                matches[i].insert((p.x, p.y));
            }
        }
    }

    for k in (1..=4).rev() {
        if solve(&matches, &middles, k) {
            println!("{}", k);
        }
    }

    Ok(())
}

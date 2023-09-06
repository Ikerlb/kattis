use std::io::{self, BufRead};
use std::cmp::max;

#[derive(Debug, Clone)]
struct Rect {
    x: usize,
    y: usize,
    w: usize,
    h: usize,
}

impl Rect {
    fn new(x: usize, y: usize, w: usize, h: usize) -> Self {
        Self {
            x,
            y,
            w,
            h,
        }
    }

    fn ul_lr(&self) -> (usize, usize, usize, usize) {
        return (self.x, self.y, self.x + self.w, self.y + self.h);
    }

    fn intersects(&self, other: &Rect) -> bool {
        let (axmn, aymn, axmx, aymx) = self.ul_lr();
        let (bxmn, bymn, bxmx, bymx) = other.ul_lr();

        let first = !((aymn <= bymn && aymx <= bymn) || (aymn >= bymx && aymx >= bymx));
        let second = !((axmn <= bxmn && axmx <= bxmn) || (axmn >= bxmx && axmx >= bxmx));
        return first && second;
    }

    fn area(&self) -> usize {
        return self.w * self.h;
    }
}


fn dfs(rects: &Vec<Rect>, i: usize, area: usize, taken: &mut Vec<usize>) -> usize {
    if i == rects.len() {
        return area;
    }
    let mut res = dfs(rects, i + 1, area, taken);
    if !taken.iter().any(|t| rects[i].intersects(&rects[*t])) {
        let mut na = rects[i].area();
        taken.push(i);
        res = max(res, dfs(rects, i + 1, area + na, taken));
        taken.pop();
    }
    return res;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|s_res| s_res.unwrap());

    let mut grid = vec![vec![false; 1000]; 1000];

    let mut i = 0;

    loop {
        let n = lines.next().unwrap().parse::<usize>().unwrap();
        if n == 0 {
            break;
        }

        let mut rects = Vec::new();

        for _ in 0..n {
            let handler = lines
                .next()
                .unwrap();
            let mut split = handler
                .split(" ")
                .map(|s| s.parse::<usize>().unwrap());
            let w = split.next().unwrap();
            let h = split.next().unwrap();
            let x = split.next().unwrap();
            let y = split.next().unwrap();
            rects.push(Rect::new(x, y, w, h));

        }

        let mut taken = Vec::new();
        println!("{}", dfs(&rects, 0, 0, &mut taken));
    }

    Ok(())
}

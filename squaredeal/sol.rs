use std::io::{self, BufRead};

#[derive(Debug)]
struct Rect {
    width: usize,
    height: usize,
}

impl Rect {
    fn new(w: usize, h: usize) -> Self {
        return Rect {
            width: w,
            height: h,
        };
    }

    fn glue_vertical(&self, other: &Self) -> Option<Self> {
        if self.height == other.height {
            return Some(Self {
                width: self.width + other.width,
                height: self.height
            });
        }
        return None;
    }

    fn glue_horizontal(&self, other: &Self) -> Option<Self>{
        if self.width == other.width {
            return Some(Self {
                width: self.width,
                height: self.height + other.height
            });
        }
        return None;
    }

    fn glue(&self, other: &Self) -> Vec<Self> {
        let mut v = Vec::new();
        if let Some(hor) = self.glue_horizontal(other) {
            v.push(hor);
        }
        if let Some(ver) = self.glue_vertical(other) {
            v.push(ver);
        }
        return v;
    }
}

fn solve(rects: &Vec<Vec<Rect>>) -> bool {
    for r1 in &rects[0] {
        for r2 in &rects[1] {
            for mid in r1.glue(r2) {
                for r3 in &rects[2] {
                    for res in r3.glue(&mid) {
                        if res.height == res.width {
                            return true;
                        }
                    }
                }
            }
        }
    }
    for r1 in &rects[2] {
        for r2 in &rects[1] {
            for mid in r1.glue(r2) {
                for r3 in &rects[0] {
                    for res in r3.glue(&mid) {
                        if res.height == res.width {
                            return true;
                        }
                    }
                }
            }
        }
    }
    return false;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let rects = stdin
        .lock()
        .lines()
        .map(|res_s| {
            let s = res_s.unwrap();
            let mut split = s
                .split(" ")
                .map(|n| n.parse::<usize>().unwrap());
            let w = split.next().unwrap();
            let h = split.next().unwrap();
            return vec![Rect::new(w, h), Rect::new(h, w)];
        })
        .collect::<Vec<_>>();

    if solve(&rects) {
        println!("YES");
    } else {
        println!("NO");
    }

    
    Ok(())
}


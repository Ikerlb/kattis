use std::io::{self, BufRead};
use std::str::FromStr;

#[derive(Debug)]
struct Point {
    x: f64,
    y: f64,
}

#[derive(Debug)]
struct Segment {
    start: Point,
    end: Point,
}

impl Point {
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    fn distance(&self, other: &Point) -> f64 {
        let dx = self.x - other.x;
        let dy = self.y - other.y;
        let dist_squared = dx * dx + dy * dy;
        dist_squared.sqrt()
    }
}

impl Segment {

    fn ccw(&self, c: &Point) -> f64 {
        let a = &self.start;
        let b = &self.end;
        (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
    }

    fn on_segment(&self, p: &Point) -> bool {
        let a = &self.start;
        let b = &self.end;
        p.x <= a.x.max(b.x) && p.x >= a.x.min(b.x) && p.y <= a.y.max(b.y) && p.y >= a.y.min(b.y)
    }

    fn intersects(&self, other: &Segment) -> bool {
        let p1 = &self.start;
        let q1 = &self.end;
        let p2 = &other.start;
        let q2 = &other.end;

        let o1 = self.ccw(p2);
        let o2 = self.ccw(q2);
        let o3 = other.ccw(p1);
        let o4 = other.ccw(q1);

        if o1 * o2 < 0.0 && o3 * o4 < 0.0 {
            // The segments intersect.
            true
        } else if o1 == 0.0 && self.on_segment(p2) {
            // p2 is on the line segment self.
            true
        } else if o2 == 0.0 && self.on_segment(q2) {
            // q2 is on the line segment self.
            true
        } else if o3 == 0.0 && other.on_segment(p1) {
            // p1 is on the line segment other.
            true
        } else if o4 == 0.0 && other.on_segment(q1) {
            // q1 is on the line segment other.
            true
        } else {
            // The segments do not intersect.
            false
        }
    }

    fn distance_to_point(&self, p: &Point) -> f64 {
        let mut dx = self.end.x - self.start.x;
        let mut dy = self.end.y - self.start.y;

        if dx == 0.0 && dy == 0.0 { // segment is a point
            return self.start.distance(p);
        }

        let mag = dx * dx + dy * dy;
        let t = ((p.x - self.start.x) * dx + (p.y - self.start.y) * dy) / mag;

        if t < 0.0 {
            dx = p.x - self.start.x;
            dy = p.y - self.start.y;
        } else if t > 1.0 {
            dx = p.x - self.end.x;
            dy = p.y - self.end.y;
        } else {
            let nx = self.start.x + t * dx;
            let ny = self.start.y + t * dy;
            dx = p.x - nx;
            dy = p.y - ny;
        }

        (dx * dx + dy * dy).sqrt()
    }

    fn distance_to_segment(&self, other: &Segment) -> f64 {
        if self.intersects(other) {
            0.0
        } else {
            let d1 = self.distance_to_point(&other.start);
            let d2 = self.distance_to_point(&other.end);
            let d3 = other.distance_to_point(&self.start);
            let d4 = other.distance_to_point(&self.end);
            d1.min(d2).min(d3).min(d4)
        }
    }

}


fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut iter = stdin.lock().lines();

    // burn first line
    iter.next();

    let lines = iter
        .collect::<io::Result<Vec<_>>>()
        .unwrap();

    let segments_pairs = lines
        .iter()
        .map(|s| {
            let v = s
                .split(' ')
                .map(|s| f64::from_str(s).unwrap())
                .collect::<Vec<_>>();
            
            let mut chunks = v.chunks(4)
                .map(|c| Segment {
                    start: Point::new(c[0], c[1]),
                    end: Point::new(c[2], c[3]),
                });

            (chunks.next().unwrap(), chunks.next().unwrap())
        })
        .collect::<Vec<_>>();

    for (fst, snd) in segments_pairs {
        println!("{:.2}", fst.distance_to_segment(&snd));
    }

    Ok(())
}

use std::io::{self, BufRead};

fn solve(w: usize, l: usize, circles: Vec<(f64, f64)>) -> Option<usize> {
    let l = l as f64;

    let whalf = w as f64 / 2.0;
    let whalf_sq = whalf * whalf;

    let epsilon = 0.00001;

    let mut intervals = circles
        .iter()
        .map(|(xc, rd)| {
            let dx = (rd * rd - whalf_sq).sqrt();
            return (xc - dx, xc + dx);
        }).collect::<Vec<_>>();

    intervals.sort_by(|a, b| a.partial_cmp(b).unwrap());

    // do interval cover
    let mut ans = 0;
    let mut covered_so_far = 0.0; 
    let mut i = 0;
    while i < intervals.len() {
        if covered_so_far >= l {
            return Some(ans);
        }
        if intervals[i].1 < covered_so_far + epsilon {
            // do nothing
        } else if intervals[i].0 < covered_so_far + epsilon {
            let mut max_r = -1.0;
            let mut max_i = i;
            let mut j = i;
            while j < intervals.len() && (intervals[j].0) < covered_so_far + epsilon {
                if intervals[j].1 > max_r {
                    max_r = intervals[j].1;
                    max_i = j;
                }
                j += 1;
            }
            ans += 1;
            covered_so_far = max_r;
            i = max_i;
        } else {
            return None;
        }
        i += 1;
    }

    if covered_so_far < l {
        return None;
    } else {
        return Some(ans);
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    while let Some(handler) = lines.next() {
        let mut iterator = handler
            .split(" ")
            .map(|s| s.parse::<usize>().unwrap());
        let n = iterator.next().unwrap();
        let l = iterator.next().unwrap();
        let w = iterator.next().unwrap();


        let circles = (0..n)
            .map(|_| {
                let handler = lines.next().unwrap();
                let mut iterator = handler
                    .split(" ")
                    .map(|s| s.parse::<f64>().unwrap());
                let xcenter = iterator.next().unwrap();
                let radius = iterator.next().unwrap();

                return (xcenter, radius);
            }).collect::<Vec<_>>();

        if let Some(res) = solve(w, l, circles) {
            println!("{}", res);
        } else {
            println!("-1");
        }
    }

    Ok(())
}

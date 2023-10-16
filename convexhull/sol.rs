use std::io::{self, BufRead, BufWriter, Write};

fn to_vec(a: &(isize, isize), b: &(isize, isize)) -> (isize, isize) {
    return (b.0 - a.0, b.1 - a.1);
}

fn cross(a: &(isize, isize), b: &(isize, isize)) -> isize {
    return (a.0 * b.1) - (a.1 * b.0);
}

fn ccw(p: &(isize, isize), q: &(isize, isize), r: &(isize, isize)) -> bool {
    return cross(&to_vec(p, q), &to_vec(p, r)) > 0;
}

fn parse_line(s: &str) -> (isize, isize) {
    let mut split = s.split(" ");
    let fst = split 
        .next()
        .unwrap()
        .parse::<isize>()
        .unwrap();
    let snd = split 
        .next()
        .unwrap()
        .parse::<isize>()
        .unwrap();
    return (fst, snd);
}

fn to_normal_form(points: &Vec<(isize, isize)>) -> Vec<(isize, isize)> {
    // remove duplicates
    let mut res = Vec::with_capacity(points.len());
    res.push(points[0].clone());
    for i in 1..points.len() {
        if points[i - 1] == points[i] {
            continue;
        } else {
            res.push(points[i].clone());
        }
    }
    return res;
}

fn convex_hull(points: &Vec<(isize, isize)>) -> Vec<(isize, isize)> {
    let mut k = 0;
    let n = points.len();
    let mut h = vec![(0, 0); 2 * n];
    for i in 0..n {
        while k >= 2 && !ccw(&h[k - 2], &h[k - 1], &points[i]) {
            k -= 1;
        }
        h[k] = points[i];
        k += 1;
    }

    let mut t = k + 1;
    let lim = if n >= 2 {
        n - 2
    } else {
        0
    };
    for i in (0..=lim).rev() {
        while k >= t && !ccw(&h[k - 2], &h[k - 1], &points[i]) {
            k -= 1;
        }
        h[k] = points[i];
        k += 1;
    }

    return h.drain(..(k - 1)).collect::<Vec<_>>();
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let stdout = io::stdout();

    let mut writer = BufWriter::new(stdout);

    loop {
        let n = lines
            .next()
            .unwrap()
            .parse::<usize>()
            .unwrap();
        if n == 0 {
            break;
        }

        let mut points = lines
            .by_ref()
            .take(n)
            .map(|s| parse_line(&s))
            .collect::<Vec<_>>();

        points.sort();

        let res = convex_hull(&to_normal_form(&points));
        writeln!(writer, "{}", res.len());
        for (a, b) in res {
            writeln!(writer, "{} {}", a, b);
        }
    }

    Ok(())
}

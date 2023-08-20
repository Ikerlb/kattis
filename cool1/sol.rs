use std::io::{BufRead, self};

fn mkmove(grid: &Vec<Vec<char>>, r: usize, c: usize, dr: isize, dc: isize) -> (usize, usize) {
    let nr = (r as isize + dr) as usize;
    let nc = (c as isize + dc) as usize;
    if grid[nr][nc] != '#' {
        return (nr, nc);
    }
    return (r, c);
}

fn direction(c: char) -> (isize, isize) {
    return match c {
        '<' => (0, -1),
        '>' => (0, 1),
        '^' => (-1, 0),
        'v' => (1, 0),
        _   => (0, 0)
    };
}

fn divisors(n: usize) -> Vec<usize> {
    return (1..=n)
        .filter(|i| n % i == 0)
        .collect();
}

// no need to return d2 as i'm using cycle
fn smallest_support(s: &Vec<char>) -> usize {
    for d1 in divisors(s.len()) {
        let is_support = s
            .iter()
            .zip(s[..d1].iter().cycle())
            .all(|(&c1, &c2)| c1 == c2);
        if is_support {
            return d1;
        }
    }
    return 0;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let grid_size = lines
        .next()
        .unwrap()
        .unwrap()
        .parse::<usize>()
        .unwrap(); 
    let init_s = lines
        .next()
        .unwrap()
        .unwrap()
        .chars()
        .collect::<Vec<char>>();
    //println!("init s {:?}", init_s);
    let init_ss = smallest_support(&init_s);
    //println!("init smallest support {:?}", init_ss);
    let s = &init_s[..init_ss]
        .iter()
        .map(|&c| c)
        .collect::<Vec<_>>();
    //println!("s {:?}", s);

    let instrs = s
        .iter()
        .map(|&c| direction(c))
        .collect::<Vec<_>>();
    //println!("instrs {:?}", instrs);

    let mut grid = lines
        .take(grid_size)
        .map(|res| res.unwrap().chars().collect::<Vec<char>>())
        .collect::<Vec<_>>();
    //println!("grid {:?}", grid);

    let mut r = 0;
    let mut c = 0;

    for rr in 0..grid_size {
        for cc in 0..grid_size {
            if grid[rr][cc] == 'R' {
                grid[rr][cc] = '.';
                r = rr;
                c = cc;
            }
        }
    }

    let mut d = vec![vec![vec![None::<usize>; s.len()]; grid_size]; grid_size];
    //println!("d {:?}", d);

    let mut operations = Vec::new();

    let mut time = 0; 
    while d[r][c][time % s.len()].is_none() {
        d[r][c][time % s.len()] = Some(time);
        let (dr, dc) = instrs[time % instrs.len()];
        let (nr, nc) = mkmove(&grid, r, c, dr, dc);
        if (nr, nc) != (r, c) {
            operations.push(time);
        }
        r = nr;
        c = nc;
        time += 1;
    }

    //println!("operations {:?}", operations);

    if let Some(prev) = d[r][c][time % s.len()] {
        let cycle_str = operations
            .iter()
            .skip_while(|&&op_time| op_time < prev)
            .map(|&op_time| s[op_time % s.len()])
            .collect::<Vec<_>>();
        //println!("cycle str: {:?}", cycle_str);
        let ss = smallest_support(&cycle_str);
        //println!("smallest support: {:?}", ss);
        println!("{}", if ss == 0 {
            1
        } else {
            ss
        });
        
    } else {
        // shouldn't happen under this parameters
        panic!();
    }

    return Ok(());
}

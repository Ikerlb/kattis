use std::cmp::{max, min};
use std::collections::HashSet;
use std::io::{self, BufRead};

fn process_order(s: String) -> Vec<usize> {
    let iter = s.trim().split(" ");
    let mut res = iter
        .map(|ns| ns.parse::<usize>().unwrap() - 1)
        .collect::<Vec<_>>();
    res.reverse();
    return res;
}

fn count(votes: &mut Vec<Vec<usize>>, dqs: &Vec<bool>) -> Vec<usize> {
    let mut counts = vec![0; dqs.len()];
    for order in votes {
        while let Some(&vote) = order.last() {
            if dqs[vote] {
                order.pop();
            } else {
                counts[vote] += 1;
                break;
            }
        }
    }
    return counts;
}

fn min_candidate(counts: &Vec<usize>, dqs: &Vec<bool>) -> usize {
    return (0..counts.len())
        .filter(|&i| !dqs[i])
        .min_by_key(|&i| (counts[i], -(i as isize)))
        .unwrap();
}

fn max_candidate(counts: &Vec<usize>, dqs: &Vec<bool>) -> usize {
    return (0..counts.len())
        .filter(|&i| !dqs[i])
        .max_by_key(|&i| (counts[i], -(i as isize)))
        .unwrap();
}

/*
 * each voting round (m)
 * we traverse all the votes (n)
 * O(n * m)
 * */
fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let first_binding = lines.next().unwrap().unwrap();
    let mut first = first_binding
        .split(" ")
        .map(|ns| ns.parse::<usize>().unwrap());
    let n = first.next().unwrap();
    let m = first.next().unwrap();
    //println!("n {}, m {}", n, m);

    let candidates = (&mut lines)
        .take(m)
        .map(|line| line.unwrap())
        .collect::<Vec<_>>();
    //println!("{:?}", candidates);

    let mut order = lines
        .map(|line_res| process_order(line_res.unwrap()))
        .collect::<Vec<_>>();
    //println!("votes order {:?}", order);

    let majority = n >> 1;

    let mut dqs = vec![false; m];
    for _ in 0..m {
        let c = count(&mut order, &dqs);
        let mn = min_candidate(&c, &dqs); 
        let mx = max_candidate(&c, &dqs); 
        //println!("counts: {:?}, mn: {}, mx: {}, {}", c, mn, mx, majority);
        if c[mx] > majority {
            println!("{}", candidates[mx]);
            break;
        } else {
            dqs[mn] = true;
        }
    }

    Ok(())
}

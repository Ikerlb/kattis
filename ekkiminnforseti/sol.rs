use std::cmp::{max, min};
use std::collections::{HashSet, BTreeSet, HashMap};
use std::io::{self, BufRead};

fn process_order(s: String) -> Vec<usize> {
    let iter = s.trim().split(" ");
    let mut res = iter
        .map(|ns| ns.parse::<usize>().unwrap() - 1)
        .collect::<Vec<_>>();
    res.reverse();
    return res;
}

/*
 * smarter brute force:
 * for each vote, maintain
 * a sorted set with the
 * number of votes each
 * candidate has
 * whenever we remove 
 * a candidate, we only
 * update those whose
 * first valid vote
 * is the candidate to remove
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

    let candidates = (&mut lines)
        .take(m)
        .map(|line| line.unwrap())
        .collect::<Vec<_>>();

    let order = lines
        .map(|line_res| process_order(line_res.unwrap()))
        .collect::<Vec<_>>();

    let mut votes: HashMap<usize, Vec<Vec<usize>>> = HashMap::new();

    let mut tree = BTreeSet::<(usize, isize)>::new();
    for mut o in order {
        if let Some(mvv) = o.pop() {
            votes.entry(mvv).or_insert(Vec::new()).push(o);
        }
    }
    for i in 0..m {
        let len = if let Some(v) = votes.get(&i) {
            v.len()
        } else {
            0
        };
        tree.insert((len, -(i as isize)));
    }

    let mut dqs = HashSet::new();

    for _ in 0..(m - 1) {
        let &(sz, mi) = tree.last().unwrap();
        if sz > (n >> 1) {
            break;
        }
        
        let (_, mi) = tree.pop_first().unwrap();
        let i = -mi as usize;
        dqs.insert(i);

        if let Some(all_i_votes) = votes.remove(&i) {
            for mut v in all_i_votes {
                while let Some(mvv) = v.pop() {
                    if dqs.contains(&mvv) {
                        continue;
                    } else {
                        let prev_size = votes[&mvv].len();
                        let mmvv = -(mvv as isize);
                        tree.remove(&(prev_size, mmvv));
                        votes.entry(mvv).and_modify(|e| e.push(v));
                        tree.insert((prev_size + 1, mmvv));
                        break;
                    }
                }
            }
        }

    }

    let (_, mi) = tree.pop_last().unwrap();
    let i = -mi as usize;

    println!("{}", candidates[i]);

    Ok(())
}

use std::io::{self, BufRead};
use std::collections::{HashMap, HashSet};

fn lasts(s: &Vec<char>) -> [isize; 26] {
    let mut res = [-1; 26];
    for (i, &c) in s.into_iter().enumerate() {
        res[c as usize - 'a' as usize] = i as isize;
    }
    return res;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|line_res| line_res.unwrap());

    let fst_line = lines.next().unwrap();
    let fst = fst_line.split(" ");
    let mut fst = fst.map(|w| w.parse::<usize>().unwrap());
    let n = fst.next().unwrap();
    let m = fst.next().unwrap();

    let dictionary = (&mut lines)
        .take(n)
        .map(|s| s.chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let plates = (&mut lines)
        .take(m)
        .map(|s| s.to_lowercase().chars().collect::<Vec<_>>())
        .collect::<Vec<_>>();

    let lasts = dictionary    
        .iter()
        .map(|s| lasts(s))
        .collect::<Vec<_>>();

    let mut d: HashMap<String, HashSet<char>> = HashMap::new();
    for p in &plates {
        let two = p[..2].iter().collect::<String>();
        let thd = p[2];
        d.entry(two).or_insert(HashSet::new()).insert(thd);
    }

    let mut done = HashMap::new();

    for (wi, w) in dictionary.iter().enumerate() {
        for i in 0..w.len() {
            for j in (i + 1)..w.len() {
                let mut to_rem = Vec::new();
                let p = format!("{}{}",w[i], w[j]);
                if let Some(thds) = d.get(&p) {
                    for &thd in thds {
                        if lasts[wi][thd as usize-'a' as usize]>j as isize {
                            to_rem.push(thd);
                        }
                    }
                }
                for thd in to_rem {
                    if let Some(hs) = d.get_mut(&p) {
                        hs.remove(&thd); 
                        done.insert(format!("{}{}", p, thd), wi);
                    }
                }
            }
        }
    }

    for pv in plates {
        let plate = pv.iter().collect::<String>(); 
        if let Some(&wi) = done.get(&plate) {
            let s = dictionary[wi].iter().collect::<String>();
            println!("{}", s);
        } else {
            println!("No valid word");
        }
    }

    Ok(())
}

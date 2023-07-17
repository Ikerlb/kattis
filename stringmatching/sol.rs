use std::io::{self, BufRead};

fn z_array(p: &Vec<char>) -> Vec<i64> {
    let mut i = 0;
    let mut j = -1;
    let m = p.len();
    let mut b = vec![0; m + 1];
    b[0] = -1;
    while i < m {
        while j >= 0 && p[i] != p[j as usize] {
            j = b[j as usize];
        }
        i += 1;
        j += 1;
        b[i] = j;
    }
    return b;
}

fn find(p: &Vec<char>, s: &Vec<char>) -> Vec<String> {
    let b = z_array(p);

    let mut i = 0;
    let mut j = 0i64;

    let m = p.len();
    let n = s.len();

    let mut res = Vec::new();
    while i < n {
        while j >= 0 && s[i] != p[j as usize] {
            j = b[j as usize];
        }
        i += 1;
        j += 1;
        if j as usize == m {
            res.push(format!("{}", i - (j as usize)));
            j = b[j as usize];
        }
    }
    return res;
}

fn main() -> io::Result<()> {
    let lines = io::stdin()
        .lock()
        .lines()
        .map(|res| res.unwrap().chars().collect::<Vec<_>>())
        .collect::<Vec<Vec<_>>>();

    for i in (0..lines.len()).step_by(2) {
        
        println!("{}", find(&lines[i], &lines[i + 1]).join(" "));    
    }

    return Ok(());
}

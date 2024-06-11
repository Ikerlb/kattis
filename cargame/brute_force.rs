use std::io::{self, BufRead};

fn index(v: &Vec<char>, c: char, start: usize) -> usize {
    for i in start..v.len() {
        if v[i] == c {
            return i
        }
    }
    return v.len();
}

fn search(word: &Vec<char>, plate: &Vec<char>) -> bool {
    let mut last = 0;
    for &p in plate {
        last = index(word, p, last) + 1;
        if last > word.len() {
            return false;
        }
    }
    return true;
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

    for plate in &plates {
        let mut res = None;
        for d in &dictionary {
            if search(d, plate) {
                res = Some(d.iter().collect::<String>());
                break;
            } 
        }
        if let Some(w) = res {
            println!("{}", w);
        } else {
            println!("No valid word");
        }
    }

    Ok(())
}

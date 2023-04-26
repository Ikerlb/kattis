use std::io::{self, Result, BufRead};
use std::collections::{BTreeMap, BTreeSet};

#[derive(PartialEq, Eq, PartialOrd, Ord, Debug)]
struct Key {
    level: usize,
    entering: isize,
    name: String
}

fn main() -> Result<()> {
    let stdin = io::stdin();
    let lines = stdin
        .lock()
        .lines()
        .collect::<Result<Vec<String>>>()?;
    let mut iter = lines.iter();

    iter.next(); // burn
        
    let mut injury_level: BTreeMap<String, (usize, isize)> = BTreeMap::new();
    let mut ordering: BTreeSet<Key> = BTreeSet::new();

    for (i, line) in iter.enumerate() {
        let mut line_iter = line.split(" ");
        match line_iter.next().clone() {
            None => continue,
            Some("0") => {
                let name = line_iter.next().unwrap().to_string();
                let level = line_iter.next().unwrap().parse().unwrap();
                let key = Key {
                    level: level,
                    entering: -(i as isize),
                    name: name.clone()
                };
                injury_level.insert(name, (level, -(i as isize)));
                ordering.insert(key);
            },
            Some("1") => {
                // update 
                let name = line_iter.next().unwrap().to_string();
                let (level, entering) = *injury_level.get(&name).unwrap(); 
                let new_level = level + line_iter.next().unwrap().parse::<usize>().unwrap();
                let previous_key = Key {
                    level: level,
                    entering: entering,
                    name: name.clone()
                };
                let key = Key {
                    level: new_level,
                    entering: entering,
                    name: name.clone()
                };
                
                ordering.remove(&previous_key);
                ordering.insert(key);

                injury_level.insert(name, (new_level, entering));
            },
            Some("2") => {
                // treat
                let name = line_iter.next().unwrap().to_string();
                let (level, entering) = *injury_level.get(&name).unwrap(); 
                let key = Key {
                    level,
                    entering: entering,
                    name: name.clone()
                };
                ordering.remove(&key);
                injury_level.remove(&name);
            },
            Some("3") => {
                /* todo arriving order */
                if let Some(last_key) = ordering.last() {
                    println!("{}", last_key.name);
                } else {
                    println!("The clinic is empty");
                }
            },
            _ => { todo!(); }
        }
    }

    Ok(())
}

use std::io::{self, BufRead};
use std::collections::HashMap;
use io::Error;

fn main() -> Result<(), Error> {
    let stdin = io::stdin();
    let lines_vec = stdin
        .lock()
        .lines()
        .collect::<Result<Vec<String>, _>>()?;
    let mut lines = lines_vec 
        .iter();

    // burn number of lines
    lines.next();
    
    let mut context: Vec<HashMap<String, String>> = Vec::new();
    context.push(HashMap::new());

    let mut lookup: HashMap<String, Vec<usize>> = HashMap::new();

    for line in lines {
        let mut words_iter = line.split(' ');
        match words_iter.next() {
            Some("DECLARE") => {
                let var_name = words_iter.next().unwrap().to_string();
                let type_name = words_iter.next().unwrap().to_string();
                let last_level = context.last_mut().unwrap();

                if let Some(res) = last_level.get(&var_name) {
                    println!("MULTIPLE DECLARATION");
                    break;
                } else  { // declare
                    last_level.insert(var_name.clone(), type_name);
                    lookup
                        .entry(var_name)
                        .or_insert(Vec::new())
                        .push(context.len() - 1);
                }
            },
            Some("TYPEOF") => {
                let var_name = words_iter.next().unwrap();
                if let Some(level_v) = lookup.get(var_name) {
                    let index = level_v.last().unwrap();
                    println!("{}", context[*index].get(var_name).unwrap());
                } else {
                    println!("UNDECLARED");
                }
            },
            Some("{") => {
                context.push(HashMap::new());
            },
            Some("}") => {
                let mut to_remove = context.pop().unwrap();
                to_remove
                    .drain()
                    .for_each(|(vn, tn)| {
                        let level = lookup
                            .get_mut(&vn)
                            .unwrap();
                        if level.len() == 1 {
                            lookup.remove(&vn);
                        } else {
                            level.pop();
                        }
                    })

            },
            _ => todo!(),
        }
    }
    Ok(())
}


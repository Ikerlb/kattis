use std::io::{self, BufRead};
use std::collections::HashMap;
use std::process;

fn main() {
    let stdin = io::stdin();
    let mut lines_iter = stdin.lock().lines();

    // burn n
    lines_iter.next();

    let mut levels: HashMap<String, Vec<usize>> = HashMap::new();
    let mut context: Vec<HashMap<String, String>> = Vec::new();

    context.push(HashMap::new());

    for r_line in lines_iter {
        let unwrapped = r_line.unwrap();
        let line = unwrapped.trim();
        let mut iter = line.split_whitespace();
        let ntok = iter.next().unwrap();
        

        match ntok {
            "{" => {
                context.push(HashMap::new());
            },
            "}" => {
                for k in context.pop().unwrap().keys() {
                    levels.get_mut(k).unwrap().pop();
                }
            },
            "DECLARE" => {
                let k = iter.next().unwrap();
                let t = iter.next().unwrap();
                let last_level = context.last_mut().unwrap();
                if last_level.contains_key(k) {
                    println!("MULTIPLE DECLARATION");
                    break;
                } else {
                    last_level.insert(k.to_string(), t.to_string());

                }
                if let Some(level) = levels.get_mut(k) {
                    level.push(context.len() - 1);
                } else {
                    let mut nv = Vec::new(); 
                    nv.push(context.len() - 1);
                    levels.insert(k.to_string(), nv);
                }
            },
            "TYPEOF" => {
                let k = iter.next().unwrap();
                let level = levels.get_mut(k);
                if level.is_some() && level.as_ref().unwrap().len() > 0 {
                    println!("{}", context[*level.unwrap().last().unwrap()].get(k).unwrap());
                } else {
                    println!("UNDECLARED");
                }
            },
            _ => panic!()
        }
    }
}

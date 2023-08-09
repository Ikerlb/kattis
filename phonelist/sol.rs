use std::io::{self, BufRead};
use std::collections::HashMap;

#[derive(Default)]
struct Node {
    d: HashMap<char,Node>,
    w: bool,
}

impl Node {
    pub fn new() -> Self {
        return Self {
            d: HashMap::new(),
            w: false 
        };
    }

    pub fn add(&mut self, w: &str) {
        let mut node = self;
        for c in w.chars() {
            let next_node = node.d.entry(c).or_insert(Node::new());
            node = next_node;
        }
        node.w = true;
    }

    pub fn is_prefix(&mut self, w: &str) -> bool {
        let mut node = self;
        for c in w.chars() {
            if node.d.contains_key(&c) {
                node = node.d.entry(c).or_default();
            } else {
                return false; // this case should never happen
            }
        }
        return node.d.len() > 0;
    }
}

fn solve(telephones: Vec<String>) -> String {
    let mut node = Node::new(); 
    for telephone in &telephones {
        node.add(telephone);
    }
    let has_prefix = telephones
        .iter()
        .any(|telephone| node.is_prefix(telephone));
    if has_prefix {
        return "NO".to_string();
    } else {
        return "YES".to_string();
    }
}

fn main() -> io::Result<()> {
    let mut lines = io::stdin()
        .lock()
        .lines()
        .filter_map(|l| l.ok());
    let tcs = lines.next().unwrap().parse::<usize>().unwrap();
    for tc in 0..tcs {
        let n = lines.next().unwrap().parse::<usize>().unwrap(); 
        let telephones = (0..n)
            .map(|i| lines.next().unwrap())
            .collect::<Vec<_>>();
        println!("{}", solve(telephones));
    }
    return Ok(());
}

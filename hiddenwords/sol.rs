use std::io::{self, BufRead};
use std::collections::HashMap;

#[derive(Clone, Debug, Default)]
struct Node {
    d: HashMap<char,Node>,
    w: Vec<usize>,
}

impl Node {
    pub fn new() -> Self {
        return Self {
            d: HashMap::new(),
            w: Vec::new(), 
        };
    }

    pub fn add(&mut self, i: usize, w: &str) {
        let mut node = self;
        for c in w.chars() {
            let next_node = node.d.entry(c).or_insert(Node::new());
            node = next_node;
        }
        node.w.push(i);
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

#[derive(Debug)]
struct Trie {
    root: Node
}

impl Trie {
    fn new() -> Self {
        Self {
            root: Node::new(),
        }
    }

    fn add(&mut self, i: usize, w: &str) {
        self.root.add(i, w);
    }
}

const DIRS: [(isize, isize); 4] = [(-1, 0), (1, 0), (0, -1), (0, 1)];

fn dfs(grid: &mut Vec<Vec<char>>, r: usize, c: usize, node: &Node, contained: &mut Vec<usize>) {
    let ni = grid.len() as isize;
    let mi = grid[0].len() as isize;

    let chr = grid[r][c];
    grid[r][c] = '_';

    if let Some(nnode) = node.d.get(&chr) {
        /*if nnode.w != -1 {
            //println!("r: {} c: {} res: {}", r, c, res);
            contained[nnode.w as usize] += 1; 
        }*/

        for &i in &nnode.w {
            contained[i] += 1;
        }

        for &(dr, dc) in &DIRS {
            let ri = r as isize + dr;
            let ci = c as isize + dc;
            if ri < 0 || ri == ni {
                continue;
            }
            if ci < 0 || ci == mi {
                continue;
            }
            let nr = ri as usize;
            let nc = ci as usize;

            dfs(grid, nr, nc, nnode, contained);

        }
    }

    grid[r][c] = chr;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let binding = lines
        .next()
        .unwrap();
    let mut split = binding
        .split(" ")
        .map(|s| s.parse::<usize>().unwrap());

    let n = split
        .next()
        .unwrap();

    let m = split
        .next()
        .unwrap();

    let mut grid = Vec::new();

    for _ in 0..n {
        let line = lines.next().unwrap();
        let v = line
            .chars()
            .collect::<Vec<_>>();
        grid.push(v);
    }

    let words = lines
        .next()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    let mut trie = Trie::new();
    let mut contained = vec![0; words];

    for (i, w) in lines.take(words).enumerate() {
        trie.add(i, &w);
    }

    for r in 0..n {
        for c in 0..m {
            dfs(&mut grid, r, c, &trie.root, &mut contained);
        }
    }

    let res = contained
        .iter()
        .map(|&f| {
            if f > 0 {
                1
            } else {
                0
            }
        })
        .sum::<usize>();

    println!("{}", res);

    return Ok(());
}

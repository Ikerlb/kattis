use std::io::{self, BufRead};
use std::collections::{HashMap};
use std::collections::hash_map::DefaultHasher;
use std::hash::{Hash, Hasher};
use std::fmt;

#[derive(Debug)]
enum Token {
    OpenPar,
    ClosedPar,
    Comma,
    Word(String),
}

fn tokenize(s: &str) -> Vec<Token> {
    let mut res = vec![];
    let mut cur = String::new();

    for c in s.chars() {
        match (c, cur.as_str()) {
            ('(', "") => res.push(Token::OpenPar), 
            (')', "") => res.push(Token::ClosedPar), 
            (',', "") => res.push(Token::Comma),
            ('(', _) => {
                res.push(Token::Word(cur.clone()));
                cur.clear();
                res.push(Token::OpenPar);
            }, 
            (')', _) => {
                res.push(Token::Word(cur.clone()));
                cur.clear();
                res.push(Token::ClosedPar);
            }, 
            (',', _) => {
                res.push(Token::Word(cur.clone()));
                cur.clear();
                res.push(Token::Comma);
            },
            _ => cur.push(c)
        }
    }
    if cur.len() > 0 {
        res.push(Token::Word(cur));
    }
    return res;
}

enum Node {
    Leaf(String, u64),
    Binary(String, Box<Node>, Box<Node>, u64),
}

impl fmt::Debug for Node {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            Self::Leaf(s, _) => write!(f, "{}", s),
            Self::Binary(s, n1, n2, _) => write!(f, "{}({:?},{:?})", s, *n1, *n2),
        }
    }
} 

impl Node {
    fn leaf(s: String) -> Self {
        let mut h = DefaultHasher::new();
        s.hash(&mut h);
        return Self::Leaf(s, h.finish());
    }

    fn binary(s: String, s1: Self, s2: Self) -> Self {
        let mut h = DefaultHasher::new();
        s.hash(&mut h);
        s1.get_hash().hash(&mut h);
        s2.get_hash().hash(&mut h);
        return Self::Binary(s, Box::new(s1), Box::new(s2), h.finish());
    }

    fn get_hash(&self) -> u64 {
        return match self {
            Self::Leaf(_, h) => *h,
            Self::Binary(_, _, _, h) => *h,
        };
    }
}

fn parse(tokens: Vec<Token>) -> Node {
    let mut s = vec![Vec::new()];

    for t in tokens {
        match t {
            Token::OpenPar => {
                s.push(Vec::new());
            },
            Token::ClosedPar => {
                let mut last = s.pop().unwrap();
                let s2 = last.pop().unwrap();
                let s1 = last.pop().unwrap();
                let n = s.len();
                let t = s[n - 1].pop().unwrap(); 
                
                let f = match t {
                    Node::Leaf(s, _) => s,
                    _ => panic!(),
                };

                let n = s.len();
                s[n - 1].push(Node::binary(f, s1, s2));
            },
            Token::Comma => continue,
            Token::Word(w) => {
                let n = s.len();
                s[n - 1].push(Node::leaf(w));
            },
        }
    }

    return s.pop().unwrap().pop().unwrap();
}

fn dfs(node: Node) -> String {
    let mut s = vec![node];
    let mut res = vec![Vec::new()]; 

    let mut d: HashMap<u64, u64> = HashMap::new();
    let mut i = 1;

    while let Some(node) = s.pop() {
        if let Some(&num) = d.get(&node.get_hash()) {
            let n = res.len();
            res[n - 1].push(format!("{}", num));
        } else {
            d.insert(node.get_hash(), i);

            i += 1;

            match node {
                Node::Leaf(f, _) => {
                    let n = res.len();
                    res[n - 1].push(f);
                },
                Node::Binary(f, left, right, _) => {
                    res.push(Vec::new());
                    s.push(*right);
                    s.push(*left);
                    let n = res.len();
                    res[n - 1].push(f);
                }
            }
        }

        /* there is always at least one */
        while let Some(last) = res.last()  {
            if last.len() != 3 {
                break;
            }

            let mut last = res.pop().unwrap();

            let s2 = last.pop().unwrap();
            let s1 = last.pop().unwrap();
            let t = last.pop().unwrap();
            let n = res.len();
            res[n - 1].push(format!("{}({},{})", t, s1, s2));
        }
    }
    return res.pop().unwrap().pop().unwrap();
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let n = lines
        .next()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    for _ in 0..n {
        let s = lines.next().unwrap();
        let tokens = tokenize(&s);
        if tokens.len() == 1 {
            println!("{}", s);
        } else {
            let node = parse(tokens);
            println!("{}", dfs(node));
        }

    }

    Ok(())
}

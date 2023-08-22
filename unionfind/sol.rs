use std::io::{BufRead, BufWriter, Write, self};
use std::mem::swap;

struct Ufs {
    parents: Vec<usize>,
    sizes: Vec<usize>
}

impl Ufs {
    pub fn new(n: usize) -> Self {
        return Self {
            parents: (0..n).collect::<Vec<usize>>(),
            sizes: vec![1; n]
        };
    }

    fn root(&mut self, mut a: usize) -> usize {
        if self.parents[a] == a {
            return a;
        } else {
            let ra = self.root(self.parents[a]);
            self.parents[a] = ra;
            return ra;
        }
    }

    pub fn find(&mut self, a: usize) -> usize {
        return self.root(a);
    }

    pub fn union(&mut self, a: usize, b: usize) -> bool {
        let mut ra = self.root(a);
        let mut rb = self.root(b); 

        if ra == rb {
            return false;
        }

        if self.sizes[ra] > self.sizes[rb] {
            swap(&mut ra, &mut rb);
        }

        self.parents[ra] = rb;
        return true;
    }

    pub fn same(&mut self, a: usize, b: usize) -> bool {
        let ra = self.root(a);
        let rb = self.root(b);

        return ra == rb;
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();

    let mut writer = io::BufWriter::new(stdout.lock());

    let lines = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;

    let mut n = lines[0]
        .split(" ")
        .next()
        .unwrap()
        .parse::<usize>()
        .unwrap();

    let mut ufs = Ufs::new(n);

    for line in lines[1..].iter() {
        let mut gen = line
            .split(" ");
        let t = gen.next().unwrap();
        let n1 = gen.next().unwrap().parse::<usize>().unwrap();
        let n2 = gen.next().unwrap().parse::<usize>().unwrap();
        
        if t == "?" && ufs.same(n1, n2) {
            write!(writer, "yes\n");
        } else if t == "?" {
            write!(writer, "no\n");
        } else {
            ufs.union(n1, n2);
        }
    }

    Ok(())
}

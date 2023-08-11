use std::io::{self, BufRead};

fn dfs(board: &mut Vec<Vec<char>>, r: usize, c: usize, target: char, k: usize) -> bool {
    if k == 0 {
        return true;
    }

    let prev = board[r][c];
    board[r][c] = '.';

     

    board[r][c] = prev;
    
}

fn solve(board: Vec<Vec<char>>, k: usize) {
    
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    let tcs = lines.next().unwrap().unwrap().parse::<usize>().unwrap();

    for _ in 0..tcs {
        let line = lines.next().unwrap().unwrap();
        let mut split = line.split(" ");
        let n = split.next().unwrap().parse::<usize>().unwrap();
        let m = split.next().unwrap().parse::<usize>().unwrap();
        let k = split.next().unwrap().parse::<usize>().unwrap();

        let mut board = vec![vec!['#'; m]; n];
        
        for r in 0..n {
            let row = lines.next().unwrap().unwrap();
            for (c, chr) in (0..m).zip(row.chars()) {
                board[r][c] = chr;
            }
        }

    }

    Ok(())
}

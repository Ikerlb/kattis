use std::io::{self, BufRead};

/*fn solve(board: Vec<Vec<usize>>, k: usize) {
    
}*/

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    let tcs = lines.next().unwrap().unwrap().parse::<usize>().unwrap();

    for _ in 0..tcs {
        let line = lines.next().unwrap().unwrap();
        let mut split = line.split(" ");
        let m = split.next().unwrap().parse::<usize>().unwrap();
        let n = split.next().unwrap().parse::<usize>().unwrap();
        let k = split.next().unwrap().parse::<usize>().unwrap();

        let mut board = vec![vec![0; m]; n];
        
        for r in 0..n {
            let row = lines.next().unwrap().unwrap();
            for (c, chr) in (0..m).zip(row.chars()) {
                if chr == 'x' {
                    board[r][c] = 1;
                } else if chr == 'o' {
                    board[r][c] = 2;
                } else {
                    board[r][c] = 0;
                }
            }
        }

        println!("{:?}", board);
        //let winner = solve(board, k)
    }

    Ok(())
}

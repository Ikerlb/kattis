use std::io::{self, BufRead};

fn format(board: &mut Vec<Vec<char>>) -> String {
    let mut res = Vec::new(); 
    for row in board.iter() {
        let s = row.iter().collect::<String>();
        res.push(s);
    }
    return res.join("\n");
}

fn dfs(b: &mut Vec<Vec<char>>, r: isize, c: isize, word: &Vec<char>, idx: usize) -> bool {

    if idx == word.len() {
        return true;
    }

    let deltas = vec![
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2),
        (1, -2),
        (2, -1),
        (2, 1),
        (1, 2)
    ];

    let n = b.len() as isize;
    let m = b[0].len() as isize;

    let prev = b[r as usize][c as usize];

    for (dr, dc) in deltas {
        let nr = r + dr;
        let nc = c + dc;
        if nr < 0 || nr >= n {
            continue;
        } else if nc < 0 || nc >= m {
            continue;
        } else if b[nr as usize][nc as usize] == word[idx] {
            if dfs(b, nr, nc, word, idx + 1) {
                return true;
            }
        }
    }

    return false;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let n = lines
        .next()
        .unwrap()?
        .parse::<usize>()
        .unwrap();

    let board_string = lines
        .next()
        .unwrap()?
        .chars()
        .collect::<Vec<_>>();
    let mut board = vec![vec!['$'; n]; n];

    for r in 0..n {
        for c in 0..n {
            board[r][c] = board_string[r * n + c];
        }
    }

    let word = "ICPCASIASG"
        .to_string()
        .chars()
        .collect::<Vec<_>>();

    let mut found = false;
    for r in 0..n {
        for c in 0..n {
            if board[r][c] == word[0] {
                if dfs(&mut board, r as isize, c as isize, &word, 1) {
                    found = true;
                    break;
                }
            }
        }
    }
    if found {
        println!("YES");
    } else {
        println!("NO");
    }

    Ok(())
}

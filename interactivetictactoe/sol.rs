use std::io::{self, BufRead};
use io::Error;

struct TicTacToe {
    : [[]]
}

fn format_board() -> String {
    
}

fn main() -> Result<(), Error> {
    let mut buffer = String::new();
    let stdin = io::stdin();
    let mut handle = stdin.lock();

    handle.read_line(&mut buffer)?;
    
    match buffer.trim() {
        "first" => {
            println!("dayum");
        },
        _       => {
            println!("dayumn't");
        }
    }

    Ok(())
}

use std::io::{BufRead, self};
use std::mem::swap;

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines()
        .map(|res_s| res_s.unwrap());

    let tcs = lines.next().unwrap().parse::<usize>().unwrap();

    let nums = (0..=10).collect::<Vec<_>>();
    let perms = permutations(&nums);

    for tc in 0..tcs {
        let handler = lines.next().unwrap();
        let mut grid_size = handler
            .split(" ")
            .map(|s| s.parse::<usize>().unwrap());
        let n = grid_size.next().unwrap();
        let m = grid_size.next().unwrap();


        let handler = lines.next().unwrap();
        let mut start_position = handler
            .split(" ")
            .map(|s| s.parse::<isize>().unwrap());
        let rs = start_position.next().unwrap();
        let cs = start_position.next().unwrap();
       
        let beeper_count = lines.next().unwrap().parse::<usize>().unwrap();
        let mut beepers = Vec::with_capacity(beeper_count);

        for i in 0..beeper_count {
            let handler = lines.next().unwrap();
            let mut pos = handler
                .split(" ")
                .map(|s| s.parse::<isize>().unwrap());
            let r = pos.next().unwrap();
            let c = pos.next().unwrap();
            beepers.push((r, c));
        }
    }

    

    Ok(())
}

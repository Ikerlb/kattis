use std::io::{self, BufRead};

/*fn solve(v: &Vec<usize>, d1: &mut Vec<usize>, d2: &mut Vec<usize>, q: isize) -> bool {
    for &n in v {
        d1[n] = 1;
        d2[n] = 1;
        if n as isize - q >= 0 {
            if d1[n - (q as usize)] == 2 {
                return true;
            } else if d1[n - (q as usize)] == 1 {
                d1[n] = 2;
            }
        }
        if n + (q as usize) < v.len() {
            if d2[n + (q as usize)] == 2 {
                return true;
            } else if d2[n + (q as usize)] == 1{
                d2[n] = 2;
            }
        }
    }
    return false;
}*/

/*fn solve(n: usize, v: &Vec<usize>, d: &Vec<usize>) -> bool {
    for i in 0..n {
        for j in (i + 1)..n {
            let k = 2*v[j] - v[i];
            if k >= 0 && k < n && d[k] > j {
                return true;
            }
        }
    }
    return false;
}*/

fn solve(n: usize, v: &Vec<usize>, d: &Vec<usize>) -> bool {
    for j in 0..n {
        for k in (j + 1)..n {
            let i = 2 * v[j] - v[k];
            if i >= 0 && i < n && d[i] < j {
                return true;
            }
        }
    }
    return false;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();

    let mut arr = vec![0; 10000];
    let mut d = vec![0; 10000];

    for line_res in lines {
        let line = line_res.unwrap(); 

        if line == "0" {
            break;
        }

        let mut p_split = line.split(": ");
        let n = p_split.next().unwrap().parse::<usize>().unwrap(); 
        let arr_s = p_split.next().unwrap();
        arr_s
            .split(" ")
            .enumerate()    
            .for_each(|(i, c)| {
                let num = c.parse::<usize>().unwrap();
                arr[i] = num;
                d[num] = i;
            });

        if solve(n, &arr, &d) {
            println!("no");
        } else {
            println!("yes");
        }
    }

    Ok(())
}

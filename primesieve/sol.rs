use std::io;

fn sieve(upto: usize) -> (usize, Vec<bool>) {
    let mut v = vec![true; upto];
    v[0] = false;
    v[1] = false;
    let mut num = 0;

    let upperLimit = (upto as f64).sqrt() as i64 + 1; 
    for i in 2..upto {
        if v[i] {
            num += 1;
            let p = i * i;
            for j in (p..upto).step_by(i) {
                v[j] = false;      
            }
        }
    }
    (num, v)
}

fn main() -> io::Result<()>{
    let mut buffer = String::new();
    io::stdin().read_line(&mut buffer)?; 
    buffer.pop();
    let first = buffer.clone();

    let vec: Vec<&str> = first.split(" ").collect();
    buffer.clear();

    if let [sn, sq] = vec[..] {
        let n = sn.parse::<usize>().unwrap();
        let q = sq.parse::<usize>().unwrap();
        let (num, v) = sieve(n + 1);
        
        println!("{}", num);
        for _ in 0..q {
            io::stdin().read_line(&mut buffer)?; 
            buffer.pop();
            let nn = buffer.parse::<usize>().unwrap();
            buffer.clear();
            let res = if v[nn] {1} else {0};
            println!("{:?}", res);
        }
    }

    Ok(())
}

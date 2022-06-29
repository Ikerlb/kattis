package main

import (
    "fmt"
    "os"
    "bufio"
)

func sieve(upto int) []bool {
    res := make([]bool, upto)
    for i := range res {
        res[i] = true
    }
    res[0] = false
    res[1] = false

    for i := 2; i * i < upto; i += 1 {
        for j := i * i; j < upto; j += i {
            res[j] = false
        }
    }

    return res
}

func main() {
    var q, n int    
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    fmt.Sscanf(sc.Text(), "%d %d", &n, &q)
    s := sieve(n)
    fmt.Println(len(s))
}

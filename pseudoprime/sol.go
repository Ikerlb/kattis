package main

import (
    "bufio"
    "fmt"
    "os"
)

func isPrime(n int, primes []int) bool {
    for i := 0; i < len(primes) && primes[i] < n; i += 1 {
        if n % primes[i] == 0 {
            return false
        }
    }
    return true
}

func sieve(n int) []int {
    p := make([]bool, n + 1)
    for i := 0; i <= n; i += 1 {
        p[i] = true    
    }

    res := make([]int, 0)
    p[0] = false
    p[1] = false
    for i := 2; i <= n; i += 1 {
        if p[i] {
            res = append(res, i)
        }
        for j := i * i; j < n; j += i  {
            p[j] = false
        }
    }
    return res
}

func pow(n, k, mod int) int {
    if k == 0 {
        return 1
    }
    half := pow(n, k / 2, mod) % mod 
    if k & 1 == 0 {
        return (half * half) % mod
    } else {
        return (((half * half) % mod) * n) % mod
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    var p, a int

    s := sieve(32000)

    for {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &p, &a)

        if p == 0 && a == 0 {
            break
        }

        if !isPrime(p, s) && (pow(a, p, p) == a) {
            fmt.Println("yes")
        } else {
            fmt.Println("no")
        }
    }
}

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func sieve(upto int) []int {
    p := make([]bool, upto + 1)
    res := make([]int, 0)
    for i := 2; i < upto + 1; i += 1 {
        if !p[i] {
            res = append(res, i)
        }
        for j := i * i; j < upto + 1; j += i {
            p[j] = true
        }
    }
    return res
}

func factors(n int, primes []int) []int {
    res := make([]int, 0)
    for i := 0; n != 1 && i < len(primes); i += 1 {
        pow := 0
        for n % primes[i] == 0 {
            pow += 1
            n /= primes[i]
        }
        if pow != 0 {
            res = append(res, pow)
        }
    }
    if n != 1 {
        res = append(res, 1)
    }
    return res
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    tcs, _ := strconv.Atoi(sc.Text())


    primes := sieve(1000)

    for tc := 0; tc < tcs; tc += 1 {
        sc.Scan()
        n, _ := strconv.Atoi(sc.Text())

        res := factors(n, primes)
        prod := 1
        for _, n := range res {
            prod *= (n + 1)
        }
        fmt.Printf("%d\n", prod - len(res))
    }
}

package main

import (
    "fmt"
    "os"
    "bufio"
    "math/big"
)

func main() {
    scanner := bufio.NewScanner(os.Stdin)
    scanner.Scan()

    var qs, n int
    fmt.Sscanf(scanner.Text(), "%d", &qs)

    MAX := 5001

    catalan := make([]*big.Int, MAX)
    catalan[0] = big.NewInt(1)
    for i := 0; i < MAX - 1; i += 1 {
        res := big.NewInt(0) 
        res.Mul(big.NewInt(int64(4 * i + 2)), catalan[i])
        res.Div(res, big.NewInt(int64(i + 2)))
        catalan[i + 1] = res
    }

    for i := 0; i < qs; i += 1 {
        scanner.Scan()

        fmt.Sscanf(scanner.Text(), "%d", &n)
        fmt.Println(catalan[n])
        //fmt.Printf("catalan[%d]=%s\n", n, catalan[n])
    }
}

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

    var n int 
    fmt.Sscanf(scanner.Text(), "%d", &n)

    MAX := 5001

    catalan := make([]*big.Int, MAX)
    catalan[0] = big.NewInt(1)
    for i := 0; i < MAX - 1; i += 1 {
        res := big.NewInt(0) 
        res.Mul(big.NewInt(int64(4 * i + 2)), catalan[i])
        res.Div(res, big.NewInt(int64(i + 2)))
        catalan[i + 1] = res
    }

    sum := big.NewInt(0)
    for k := 0; k <= n; k += 1 {
        p := big.NewInt(1)
        p.Mul(catalan[k], catalan[n - k])
        sum.Add(sum, p)
    }
    fmt.Printf("%d\n", sum)
}

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "math"
)

func isSquareNumber(n int) int {
	sq := math.Sqrt(float64(n))
    isq := int(sq)
    if isq * isq == n {
        return int(sq)
    } else {
        return -1
    }
}

func sort(n, m int) (int, int) {
    if n < m {
        return n, m
    } else {
        return m, n
    }
}


func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    d, _ := strconv.Atoi(sc.Text())

    for i := 0; i <= d; i += 1 {
        delta := i * i - d
        sq := isSquareNumber(delta)
        //fmt.Printf("i -> %d, sq -> %d, delta -> %d\n", i, sq, delta)
        if sq >= 0 {
            n, m := sort(i, sq)
            fmt.Printf("%d %d\n", n, m)
            os.Exit(0)
        }
    }
    fmt.Println("impossible")
}

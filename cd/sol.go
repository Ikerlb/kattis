package main

import (
    "fmt"
    "os"
    "bufio"
    "strconv"
)

func solve(jack, jill []int, n, m int) int {
    j := 0
    res := 0
    for i := 0; i < n; i += 1 {
        for ; j < m && jill[j] < jack[i]; j += 1 {}
        if jack[i] == jill[j] {
            res += 1
        }
    }
    return res
}

func main() {
    sc := bufio.NewScanner(os.Stdin)

    jack := make([]int, 2000000)
    jill := make([]int, 2000000)
    var n, m int

    for sc.Scan() {
        fmt.Sscanf(sc.Text(), "%d %d", &n, &m)
        if n == 0 && m == 0 {
            break
        }
        for i := 0; i < n; i += 1 {
            sc.Scan()
            v, _ := strconv.Atoi(sc.Text())
            jack[i] = v
        }

        for j := 0; j < m; j += 1 {
            sc.Scan()
            v, _ := strconv.Atoi(sc.Text())
            jill[j] = v
        }

        fmt.Printf("%d\n", solve(jack, jill, n, m))
    }
}

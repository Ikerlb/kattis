package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

func abs(x int) int{
    if x < 0 {
        return -x
    } else {
        return x
    }
}

func query(arr []int, target int) int {
    rdiff, res := 10000000, -1
    for _, n := range arr {
        if diff := abs(target - n); diff < rdiff {
            rdiff = diff
            res = n 
        }
    }
    return res
}

func main() { 
    sc := bufio.NewScanner(os.Stdin)
    tc := 1
    for sc.Scan() {
        fmt.Printf("Case %d:\n", tc)
        n, _ := strconv.Atoi(sc.Text())
        arr := make([]int, n)
        for i := 0; i < n; i += 1 {
            sc.Scan()
            num, _ := strconv.Atoi(sc.Text())
            arr[i] = num   
        }

        sums := make([]int, 0)
        for i := 0; i < n; i += 1 {
            for j := i + 1; j < n; j += 1 {
                sums = append(sums, arr[i] + arr[j])
            }
        }

        sc.Scan()
        m, _ := strconv.Atoi(sc.Text())
        for i := 0; i < m; i += 1 {
            sc.Scan()
            target, _ := strconv.Atoi(sc.Text())
            fmt.Printf("Closest sum to %d is %d.\n", target, query(sums, target))
        }
        tc += 1 
    }
}

package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "sort"
)

// return the index, handle
// the edgecase elsewhere
func search(arr []int, target int) int {
    l := 0
    r := len(arr) - 1
    for l < r {
        m := (l + r) >> 1
        if arr[m] < target {
            l = m + 1
        } else {
            r = m
        }
    }
    return l
}

func Abs(x int) int {
    if x < 0 {
        return -x
    } else {
        return x
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    var n, m int
    fmt.Sscanf(sc.Text(), "%d %d", &n, &m)

    arr := make([]int, n)
    for i := 0; i < n; i += 1 {
        sc.Scan()
        v, _ := strconv.Atoi(sc.Text())
        arr[i] = v
    }
    sort.Ints(arr)

    res := 0
    for i := 0; i < m; i += 1 {
        sc.Scan()
        q, _ := strconv.Atoi(sc.Text())
        k := search(arr, q)
        res += Abs(arr[k] - q)
    }
    fmt.Println(res)
}

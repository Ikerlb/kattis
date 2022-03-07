package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "sort"
)

func firstGreaterThan(arr []int, target int) int {
    l, r := 0, len(arr) - 1
    res := len(arr)
    for l <= r {
        m := l + ((r - l) / 2);
        if arr[m] >= target {
            res = m
            r = m - 1
        } else {
            l = m + 1
        }
    }
    return res
}

func lastSmallerThan(arr []int, target int) int {
    l, r := 0, len(arr) - 1
    res := -1
    for l <= r {
        m := l + int((r - l) / 2);
        if arr[m] <= target {
            res = m
            l = m + 1
        } else {
            r = m - 1
        }
    }
    return res
}

func solve(storesByItems map[string][]int, items []string) ([]int, bool){
    res := make([]int, 0)
    prev := 0
    for _, v := range items {
        idx := firstGreaterThan(storesByItems[v], prev)
        //fmt.Printf("finding %d in %v = %d\n", prev, storesByItems[v], idx)
        if idx >= len(storesByItems[v]) {
            return res, false
        } else {
            prev = storesByItems[v][idx]
            res = append(res, prev)
        }
    }
    return res, true
}


func solveBackwards(storesByItems map[string][]int, items []string) ([]int, bool){
    res := make([]int, 0)
    prev := int(^uint(0) >> 1)

    for i := (len(items) - 1); i >= 0; i -= 1 {
        v := items[i]
        idx := lastSmallerThan(storesByItems[v], prev)
        if idx == -1 {
            return res, false
        } else {
            prev = storesByItems[v][idx]
            res = append(res, prev)
        }
    }
    return res, true
}

func equal(a, b []int) bool {
    if len(a) != len(b) {
        return false
    }
    for i, j := 0, (len(a) - 1); i < len(a) && j >= 0; i, j = i+1, j-1 {
        if a[i] != b[j] {
            return false
        }
    }
    return true
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    //n, _ := strconv.Atoi(sc.Text())
    //fmt.Printf("%d\n", n)

    sc.Scan()
    k, _ := strconv.Atoi(sc.Text())

    storesByItems := make(map[string][]int)

    for j := 0; j < k; j += 1 {
        var i int
        var item string
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %s", &i, &item)
        storesByItems[item] = append(storesByItems[item], i)
    }

    for _, v := range storesByItems {
        sort.Ints(v)
    }

    //fmt.Printf("%v\n", storesByItems)

    sc.Scan()
    m, _ := strconv.Atoi(sc.Text())

    items := make([]string, m)

    for j := 0; j < m; j += 1 {
        sc.Scan()
        items[j] = sc.Text()
    }

    //fmt.Printf("%v\n", items)

    res1, possible := solve(storesByItems, items)

    if !possible {
        fmt.Println("impossible")
    } else {
        res2, possible := solveBackwards(storesByItems, items)
        //fmt.Printf("%v\n", res1)
        //fmt.Printf("%v\n", res2)
        if !possible || equal(res1, res2) {
            fmt.Println("unique")
        } else {
            fmt.Println("ambiguous")
        }
    }
}

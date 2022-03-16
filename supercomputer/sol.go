package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

type Fenwick []int

func NewFenwick(n int) Fenwick {
    arr := make([]int, n + 1)
    return Fenwick(arr)
}

func (ft Fenwick) Add(i, delta int) {
    for i = i + 1; i < len(ft); i += i & -i {
        ft[i] += delta
    }
}

func (ft Fenwick) query(i int) int {
    res := 0
    for ; i > 0; i -= i & -i {
        res += ft[i]
    }
    return res
}

func (ft Fenwick) Query(l, r int) int {
    return ft.query(r + 1) - ft.query(l)
}

func (ft Fenwick) Print() {
    fmt.Printf("Scanner\n")
    for i := 0; i < len(ft) - 1; i += 1 {
        fmt.Printf("%d %d\n", i, ft.Query(i, i))
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Split(bufio.ScanWords)

    writer := bufio.NewWriter(os.Stdout)
    defer writer.Flush()

    sc.Scan()
    n, _ := strconv.Atoi(sc.Text())
    sc.Scan()
    k, _ := strconv.Atoi(sc.Text())

    ft := NewFenwick(n)

    for j := 0; j < k; j += 1 {
        sc.Scan()

        if sc.Text() == "F" {
            sc.Scan()
            i, _ := strconv.Atoi(sc.Text())
            i -= 1
            if ft.Query(i, i) == 0 {
                ft.Add(i, 1)
            } else {
                ft.Add(i, -1)
            }
        } else {
            sc.Scan()
            l, _ := strconv.Atoi(sc.Text())
            sc.Scan()
            r, _ := strconv.Atoi(sc.Text())
            fmt.Fprintf(writer, "%d\n", ft.Query(l - 1, r - 1))
        }
    }
}

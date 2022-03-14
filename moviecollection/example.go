package main

import (
    "fmt"
)

type Fenwick []int

func NewFenwick(n int) Fenwick{
    arr := make([]int, n + 1)
    return Fenwick(arr)
}

func (ft Fenwick) query(i int) int {
    res := 0
    for ; i > 0; i -= (i & -i) {
        res += ft[i]
    }
    return res
}

func (ft Fenwick) Query(l, r int) int {
    return ft.query(r + 1) - ft.query(l)
}

func (ft Fenwick) Add(i, delta int) {
    for i = i + 1; i < len(ft); i += (i & -i) {
        ft[i] += delta
    }
}

func (ft Fenwick) RangeUpdate(i, j, v int) {
    ft.Add(i, v)
    ft.Add(j + 1, -v)
}

func main() {
    ft := NewFenwick(10)
    ft.RangeUpdate(0, 10, 1)

    for i := 0; i < 10; i += 1 {
        fmt.Printf("%d -> %d\n", i, ft.query(i + 1))
    }

    ft.RangeUpdate(0, 5, 1)

    for i := 0; i < 10; i += 1 {
        fmt.Printf("%d -> %d\n", i, ft.query(i + 1))
    }
}

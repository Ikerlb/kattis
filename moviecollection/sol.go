package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
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

func (ft Fenwick) RangeUpdate(i, j , v int) {
    ft.Add(i, v)
    ft.Add(j + 1, -v)
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Split(bufio.ScanWords)
    sc.Scan()


    tcs, _ := strconv.Atoi(sc.Text())
    for tc := 0; tc < tcs; tc += 1 {
        sc.Scan()
        m, _ := strconv.Atoi(sc.Text())
        sc.Scan()
        r, _ := strconv.Atoi(sc.Text())


        res := make([]string, r)
        last := make([]int, m)
        ft := NewFenwick(r + m)
        for i := 0; i < m; i += 1 {
            last[i] = r + i
            ft.Add(r + i, 1)
        }

        for i := 0; i < r; i += 1 {
            sc.Scan()
            q, _ := strconv.Atoi(sc.Text())
            li := last[q - 1]
            res[i] = fmt.Sprintf("%d", ft.query(li))
            ft.Add(li, -1)
            ft.Add(r - i - 1, 1)
            last[q - 1] = r - i - 1
        }

        fmt.Printf("%s\n", strings.Join(res, " "))
    }
}

package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
)

// if i wanted to get this done
// as soon as possible, i would 
// probably just use 6 fenwick trees!

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

func main() {
    sc := bufio.NewScanner(os.Stdin)
    maxCapacity := 200200 //1 byte * 200 000
    buf := make([]byte, maxCapacity)
    sc.Buffer(buf, maxCapacity)

    sc.Scan()

    var n, q, op, fst, snd int
    fmt.Sscanf(sc.Text(), "%d %d", &n, &q)

    values := make([]int, 6)
    sc.Scan()
    for i, v := range strings.Split(sc.Text(), " ") {
        val, _ := strconv.Atoi(v)
        values[i] = val
    }

    trees := []Fenwick{
        NewFenwick(n),
        NewFenwick(n),
        NewFenwick(n),
        NewFenwick(n),
        NewFenwick(n),
        NewFenwick(n),
    }

    types := make([]int, n)

    sc.Scan()
    for i, gem := range sc.Text() {
        types[i] = (int(gem) - '0') - 1
        trees[types[i]].Add(i, 1)
    }

    for i := 0; i < q; i += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d %d", &op, &fst, &snd)

        switch op {
        case 1:
            fst -= 1
            snd -= 1

            trees[types[fst]].Add(fst, -1) // remove from prev tree
            types[fst] = snd
            trees[snd].Add(fst, 1) // add to new tree
        case 2:
            fst -= 1
            values[fst] = snd
        default:
            fst -= 1
            snd -= 1
            res := 0
            for g := 0; g < len(values); g += 1 {
                res += values[g] * trees[g].Query(fst, snd)
            }
            fmt.Printf("%d\n", res)
        }
    }
}

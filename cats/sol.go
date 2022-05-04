package main

import (
    "fmt"
    "sort"
    "bufio"
    "os"
    "strconv"
)

type Dsu struct {
    Parents []int;
}

func NewDsu(n int) Dsu {
    p := make([]int, n)
    for i := 0; i < n; i += 1 {
        p[i] = i
    }
    return Dsu{
        p,
    }
}

func (dsu Dsu) Root(a int) int {
    /*DO ITER VERSION*/
    if dsu.Parents[a] == a {
        return a
    } else {
        ra := dsu.Root(dsu.Parents[a])
        dsu.Parents[a] = ra
        return ra
    }
}

func (dsu Dsu) Union(a, b int) bool {
    ra := dsu.Root(a)
    rb := dsu.Root(b)

    if ra == rb {
        return false
    } else {
        dsu.Parents[ra] = rb
        return true
    }
}

type Edge struct {
    C1, C2, D int;
}

type Edges []Edge

func (e Edges) Len() int {
    return len(e)
}

func (e Edges) Swap(i, j int) {
    e[i], e[j] = e[j], e[i]
}

func (e Edges) Less(i, j int) bool {
    return e[i].D < e[j].D   
}

func main() {
    var C, M, c1, c2, d int
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    tcs, _ := strconv.Atoi(sc.Text())
    for tc := 0; tc < tcs; tc += 1 {
        sc.Scan()    
        fmt.Sscanf(sc.Text(), "%d %d", &M, &C) 

        lim := (C * (C - 1)) >> 1
        s := make([]Edge, lim)
        dsu := NewDsu(C)
        for c := 0; c < lim; c += 1 {
            sc.Scan()
            fmt.Sscanf(sc.Text(), "%d %d %d", &c1, &c2, &d)
            s[c] = Edge{c1, c2, d}
        }
        sort.Sort(Edges(s))

        total := 0
        for i := 0; i < len(s); i += 1 {
            if !dsu.Union(s[i].C1, s[i].C2) {
                continue
            } else {
                total += s[i].D        
            }
        }
        if M - C - total >= 0 {
            fmt.Println("yes")
        } else {
            fmt.Println("no")
        }
    }
}

package main

import (
    "fmt"
    "os"
    "bufio"
    "sort"
    "strconv"
    "strings"
)

type Dsu struct {
    Parents []int
}

func NewDsu(n int) Dsu {
    p := make([]int, n)
    for i := 0; i < n; i += 1{
        p[i] = i 
    }
    return Dsu{ p }
}

func (dsu Dsu) Union(a, b int) bool {
    ra := dsu.root(a)
    rb := dsu.root(b)
    if ra == rb {
        return false
    }
    dsu.Parents[ra] = rb
    return true
}

func (dsu Dsu) root(a int) int {
    r := a
    for dsu.Parents[r] != r {
        r = dsu.Parents[r]
    }
    for dsu.Parents[a] != r {
        a, dsu.Parents[a] = dsu.Parents[a], r
    }
    return r
}

func (dsu Dsu) Find(a int) int {
    return dsu.root(a)
}

type Edge struct {
    N1, N2, W int
}

type Edges []Edge

func (e Edges) Len() int {
    return len(e)
}

func (e Edges) Swap(i, j int) {
    e[i], e[j] = e[j], e[i]
}

func (e Edges) Less(i, j int) bool {
    return e[i].W < e[j].W
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    n, _ := strconv.Atoi(sc.Text())
    edges := make([]Edge, 0)
    for r := 0; r < n; r += 1 {
        sc.Scan()
        line := sc.Text()
        c := 0
        for _, sw := range strings.Split(line, " ") {
            if c >= r {
                break
            }
            w, _ := strconv.Atoi(sw)
            edges = append(edges, Edge{c, r, w}) 
            c += 1
        }
    }

    sort.Sort(Edges(edges))

    dsu := NewDsu(n)

    for i := 0; i < len(edges); i += 1 {
        e := edges[i]
        if !dsu.Union(e.N1, e.N2) {
            continue    
        } else {
            fmt.Printf("%d %d\n", e.N1 + 1, e.N2 + 1)
        }
    }
}

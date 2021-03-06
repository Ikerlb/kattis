package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

type UnionFind struct {
	root []int
	size []int
}

func New(size int) *UnionFind {
	return new(UnionFind).init(size)
}

func (uf *UnionFind) init(size int) *UnionFind {
	uf = new(UnionFind)
	uf.root = make([]int, size)
	uf.size = make([]int, size)

	for i := 0; i < size; i++ {
		uf.root[i] = i
		uf.size[i] = 1
	}

	return uf
}

func (uf *UnionFind) Union(p int, q int) {
	qRoot := uf.Root(q)
	pRoot := uf.Root(p)

    if qRoot == pRoot {
        return
    }

	if uf.size[qRoot] < uf.size[pRoot] {
		uf.root[qRoot] = uf.root[pRoot]
		uf.size[pRoot] += uf.size[qRoot]
	} else {
		uf.root[pRoot] = uf.root[qRoot]
		uf.size[qRoot] += uf.size[pRoot]
	}
}

func (uf *UnionFind) Root(p int) int {
	if p > len(uf.root)-1 {
		return -1
	}

	for uf.root[p] != p {
		uf.root[p] = uf.root[uf.root[p]]
		p = uf.root[p]
	}

	return p
}

// Root or Find
func (uf *UnionFind) Find(p int) int {
	return uf.Root(p)
}

// Check if items p,q are connected
func (uf *UnionFind) Connected(p int, q int) bool {
	return uf.Root(p) == uf.Root(q)
}

func concoct(ingredients []int, ufs *UnionFind) int {
    group := make(map[int]bool)
    res := 0
    for _, i := range ingredients {
        g := ufs.Root(i)
        if _, e := group[g]; !e {
            group[g] = true
            res += ufs.size[g]
        }
    }
    if len(ingredients) == res {
        g := ufs.Root(ingredients[0])
        for k, _ := range group {
            ufs.Union(k, g)
        }
        return 1
    }
    return 0
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Split(bufio.ScanWords)
    sc.Scan()

    n, _ := strconv.Atoi(sc.Text())

    ufs := New(500001)
    res := 0

    for i := 0; i < n; i += 1 {
        sc.Scan()
        m, _ := strconv.Atoi(sc.Text())
        ingredients := make([]int, m)

        for j := 0; j < m; j += 1 {
            sc.Scan()
            nn, _ := strconv.Atoi(sc.Text())
            ingredients[j] = nn
        }
        res += concoct(ingredients, ufs)
    }

    fmt.Printf("%v\n", res)
}

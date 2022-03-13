package main

import (
    "fmt"
    "bufio"
    "os"
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

func (uf *UnionFind) Find(p int) int {
	return uf.Root(p)
}

func (uf *UnionFind) Connected(p int, q int) bool {
	return uf.Root(p) == uf.Root(q)
}

func max(a, b int) int {
    if a > b {
        return a
    } else {
        return b
    }
}

func (uf *UnionFind) Size(p int) int {
    rp := uf.Root(p)
    return uf.size[rp]
}

func (uf *UnionFind) Decrement(p int) {
    rp := uf.Root(p)
    uf.size[rp] = max(uf.size[rp] - 1, 0)
}

func main() {
    writer := bufio.NewWriter(os.Stdout)
    defer writer.Flush()

    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    var items, drawers, a, b int
    fmt.Sscanf(sc.Text(), "%d %d", &items, &drawers)

    ufs := New(drawers)

    for i := 0; i < items; i += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &a, &b)
        a -= 1
        b -= 1
        if ufs.Size(a) + ufs.Size(b) > 0 {
            ufs.Union(a, b)
            ufs.Decrement(a)
            fmt.Fprintf(writer, "LADICA\n")
        } else {
            fmt.Fprintf(writer, "SMECE\n")
        }
    }
}

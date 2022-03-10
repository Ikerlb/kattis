package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "container/heap"
)

type HeapElem struct {
    weight, node int
}

type Heap []HeapElem

func (h Heap) Len() int {
    return len(h)
}

func (h Heap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h Heap) Less(i, j int) bool {
    if h[i].weight < h[j].weight {
        return true
    } else if h[i].weight > h[j].weight {
        return false
    } else {
        return h[i].node < h[j].node
    }
}

func (h *Heap) Push(x interface{}) {
    *h = append(*h, x.(HeapElem))
}

func (h *Heap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type Adjacency struct {
    node, weight int
}

func Max(arr []int) int {
    m := 0
    for _, n := range arr {
        if n > m {
            m = n
        }
    }
    return m
}

func djikstra(g map[int][]Adjacency, h *Heap, dists []int) {
    for _, he := range *h {
        dists[he.node] = 0
    }
    for len(*h) > 0 {
        he := heap.Pop(h).(HeapElem)
        for _, adj := range g[he.node] {
            if he.weight + adj.weight < dists[adj.node] {
                heap.Push(h, HeapElem{he.weight + adj.weight, adj.node})
                dists[adj.node] = he.weight + adj.weight
            }
        }
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)

    sc.Scan()
    tc, _ := strconv.Atoi(sc.Text())
    sc.Scan() // burn empty line
    sc.Text()

    for t := 0; t < tc; t += 1 {
        var fs, n, from, to, weight int
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &fs, &n)

        graph := make(map[int][]Adjacency)
        h := &Heap{}
        heap.Init(h)

        for f := 0; f < fs; f += 1{
            sc.Scan()
            val, _ := strconv.Atoi(sc.Text())
            heap.Push(h, HeapElem{0, val - 1})
        }
        for sc.Scan() {
            var l string
            if l = sc.Text(); l == "" {
                break
            }
            fmt.Sscanf(l, "%d %d %d", &from, &to, &weight)
            from -= 1
            to -= 1
            graph[from] = append(graph[from], Adjacency{to, weight})
            graph[to] = append(graph[to], Adjacency{from, weight})
        }


        dists := make([]int, n)
        ogDists := make([]int, n)
        inf := int((^uint(0)) >> 1)
        for i, _ := range dists {
            dists[i] = inf
        }
        djikstra(graph, h, dists)
        copy(ogDists, dists)

        var max, maxIdx int
        max = inf

        for i := 0; i < n; i += 1 {
            heap.Push(h, HeapElem{0, i})
            djikstra(graph, h, dists)

            cm := Max(dists)
            if cm < max {
                max = cm
                maxIdx = i
            }
            copy(dists, ogDists)
        }
        fmt.Printf("%d\n", maxIdx + 1)
    }
}

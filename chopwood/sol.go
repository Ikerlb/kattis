package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "container/heap"
)

// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

type intPair struct {
    fst, snd int
}

func verify(l []intPair) bool {
    counter := make(map[int]int)
    for _, n := range l {
        counter[n.fst] += 1
        counter[n.snd] += 1
    }

	h := &IntHeap{}
	heap.Init(h)

    for k, v := range counter {
        if v == 1 {
            heap.Push(h, k)
        }
    }

    for _, n := range l {
        node := heap.Pop(h).(int)
        if node != n.fst {
            return false
        }
        if counter[n.fst] != 1 {
            return false
        }
        counter[n.snd] -= 1
        if counter[n.snd] == 1 {
            heap.Push(h, n.snd)
        }
    }
    return true
}

func build(l []int) []intPair {
	h := &IntHeap{}
	heap.Init(h)

    counter := make(map[int]int)
    for i := 1; i <= len(l) + 1; i += 1{
        counter[i] = 0
    }
    for _, n := range l {
        counter[n] += 1
    }

    for k, v := range counter {
        if v == 0 {
            heap.Push(h, k)
        }
    }

    res := make([]intPair, len(l))
    for i, n := range l {
        res[i] = intPair{heap.Pop(h).(int), n}
        counter[n] -= 1
        if counter[n] == 0 {
            heap.Push(h, n)
        }
    }
    return res
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    n, _ := strconv.Atoi(sc.Text())

    l := make([]int, n)
    for i := 0; i < n; i += 1 {
        sc.Scan()
        v, _ := strconv.Atoi(sc.Text())
        l[i] = v
    }

    res := build(l)

    if verify(res) {
        for _, n := range res  {
            fmt.Printf("%d\n", n.fst)
        }
    } else {
        fmt.Printf("Error\n")
    }
}

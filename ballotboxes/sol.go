package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"

    "container/heap"
)

type Item struct {
    ratio, population, ballots, index int
}

type PriorityQueue []*Item

func (pq PriorityQueue) Len() int {
    return len(pq)
}

func (pq PriorityQueue) Less(i, j int) bool {
    return pq[i].ratio > pq[j].ratio
}

func (pq PriorityQueue) Swap(i, j int) {
    pq[i], pq[j] = pq[j], pq[i]
    pq[i].index = i
	pq[j].index = j
}

func (pq *PriorityQueue) Push(x interface{}) {
	n := len(*pq)
	item := x.(*Item)
	item.index = n
	*pq = append(*pq, item)
}

func (pq *PriorityQueue) Pop() interface{} {
	old := *pq
	n := len(old)
	item := old[n-1]
	old[n-1] = nil  // avoid memory leak
	item.index = -1 // for safety
	*pq = old[0 : n-1]
	return item
}

func divmod(numerator, denominator int) (quotient, remainder int) {
    quotient = numerator / denominator 
    remainder = numerator % denominator
    return
}

func (pq *PriorityQueue) addOneBallot(item *Item) {
	item.ballots += 1
    d, m := divmod(item.population, item.ballots)
	if m > 0{
        item.ratio = d + 1
    } else {
        item.ratio = d
    }
	heap.Fix(pq, item.index)
}

func main() {
    sc := bufio.NewScanner(os.Stdin)

    for i := 0; i < 3; i += 1 {
        var cities, ballots int
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &cities, &ballots)

        if cities == -1 && ballots == -1 {
            break
        }

        pq := make(PriorityQueue, cities)
        for c := 0; c < cities; c += 1 {
            sc.Scan()
            pop, _ := strconv.Atoi(sc.Text())
            //    ratio, population, ballots, index int
            pq[c] = &Item{
                ratio: pop,
                population: pop,
                ballots: 1,
                index: c,
            }
            ballots -= 1
        }

        heap.Init(&pq)
        for b := 0; b < ballots; b += 1 {
            pItem := pq[0]
            pq.addOneBallot(pItem)
        }
        fmt.Printf("%d\n", pq[0].ratio)
        sc.Scan() // scan empty line
    }

}

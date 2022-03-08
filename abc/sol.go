package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func main() {
	sc := bufio.NewScanner(os.Stdin)

	var fst, snd, thd int
	sc.Scan()
	fmt.Sscanf(sc.Text(), "%d %d %d", &fst, &snd, &thd)

	arr := [3]int{fst, snd, thd}
	sort.Ints(arr[:])

	d := map[byte]int{
		'A': 0,
		'B': 1,
		'C': 2,
	}

	sc.Scan()
	s := sc.Text()
	fmt.Printf("%d %d %d\n", arr[d[s[0]]], arr[d[s[1]]], arr[d[s[2]]])
}

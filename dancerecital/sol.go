package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

// Perm calls f with each permutation of a.
func Perm(a []map[rune]bool, f func([]map[rune]bool)) {
    perm(a, f, 0)
}

// Permute the values at index i to len(a)-1.
func perm(a []map[rune]bool, f func([]map[rune]bool), i int) {
    if i > len(a) {
        f(a)
        return
    }
    perm(a, f, i+1)
    for j := i + 1; j < len(a); j++ {
        a[i], a[j] = a[j], a[i]
        perm(a, f, i+1)
        a[i], a[j] = a[j], a[i]
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    n, _ := strconv.Atoi(sc.Text())    

    routines := make([]map[rune]bool, n)
    for i := 0; i < n; i += 1 {
        sc.Scan()
        m := make(map[rune]bool)
        for _, c := range sc.Text()  {
            m[c] = true
        }
        routines[i] = m
    }

    m := 1000000000
    Perm(routines, func(arr []map[rune]bool){
        res := 0
        for i := 0; i < len(arr) - 1; i += 1 {
            for k, _ := range arr[i] {
                if _, e := arr[i + 1][k]; e {
                    res += 1
                }
            }
        }
        if res < m {
            m = res
        }
    })
    fmt.Printf("%d\n", m)
}

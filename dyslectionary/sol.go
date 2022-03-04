package main

import (
    "sort"
    "bufio"
    "os"
    //"strings"
    "fmt"
)

func reverse(b []byte) string {
    n := len(b)
    for i := 0; i < n >> 1; i += 1 {
        b[i], b[n - 1 - i] = b[n - 1 - i], b[i]
    }
    return string(b[:])
}

func sortAndPrint(arr []string, maxLength int) {
    sort.Strings(arr)
    for _, n := range arr {
        fmt.Printf("%*s\n", maxLength,  reverse([]byte(n)))
    }
}

func max(x, y int) int {
    if x < y {
        return y
    }
    return x
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    arr := make([]string, 0)
    maxLength := 0

    for sc.Scan() {
        b := sc.Bytes()
        if len(b) == 0 {
            sortAndPrint(arr, maxLength)
            fmt.Printf("\n")

            arr = make([]string, 0)
            maxLength = 0
        } else {
            arr = append(arr, reverse(b))
            maxLength = max(maxLength, len(arr[len(arr) - 1]))
        }
    }
    sortAndPrint(arr, maxLength)
}

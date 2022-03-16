package main

import (
    "fmt"
    "strings"
    //"strconv"
)

func H(prev int64, transaction string, token int64) int64 {
    v := prev
    for _, c := range transaction {
        v = (v * 31 + int64(c)) % 1000000007
    }
    return (v * 7 + token) % 1000000007
}

func main() {
    for i := 1; i < 1000; i += 1 {
        //fmt.Printf("%-10s yeah\n", strconv.Itoa(i))
        s := fmt.Sprintf("%-10d\n", i)
        fmt.Printf(strings.Replace(s, " ", "0", -1))
    }
}

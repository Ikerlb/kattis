package main

import (
    "fmt"
    "strconv"
    "bufio"
    "os"
)

func main() {
    sc := bufio.NewScanner(os.Stdin) 
    sc.Split(bufio.ScanWords)

    sc.Scan()
    n, _ := strconv.Atoi(sc.Text())
    m := make(map[int]int)
    for i := 0; i < n; i += 1 {
        sc.Scan()
        num, _ := strconv.Atoi(sc.Text())
        if _, e := m[num]; e {
            m[num] = -1 
        } else {
            m[num] = i
        }
    }
    for i := 6; i >= 1; i -= 1 { 
        if v, e := m[i]; e && v != -1 {
            fmt.Println(v + 1)
            os.Exit(0)
        }
    }
    fmt.Println("none")
}

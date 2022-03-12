package main

import (
    "fmt"
    "bufio"
    "os"
)

func main() {
    sc := bufio.NewScanner(os.Stdin)

    n := 8
    cols := map[int]bool{}
    ldiag := map[int]bool{}
    rdiag := map[int]bool{}
    for r := 0; r < n; r += 1 {
        sc.Scan()
        row := false
        for c, ch := range sc.Text() {
            if ch == '*' {
                if row {
                    fmt.Println("invalid")
                    os.Exit(0)
                }
                if _, ee := cols[c]; ee {
                    fmt.Println("invalid")
                    os.Exit(0)
                }
                rd := r + c
                if _, ee := rdiag[rd]; ee {
                    fmt.Println("invalid")
                    os.Exit(0)
                }
                ld := n + r - c
                if  _, ee := ldiag[ld]; ee {
                    fmt.Println("invalid")
                    os.Exit(0)
                }

                row = true
                ldiag[ld] = true
                rdiag[rd] = true
                cols[c] = true
            }
        }
    }
    if len(cols) != n {
        fmt.Println("invalid")
    } else {
        fmt.Println("valid")
    }
}

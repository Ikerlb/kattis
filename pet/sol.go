package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
)

func main() {
    sc := bufio.NewScanner(os.Stdin)
    bi := -1
    bs := 0
    for i := 0; i < 5; i += 1 {
        sc.Scan()
        s := 0
        for _, str := range strings.Split(sc.Text(), " ") {
            n, _ := strconv.Atoi(str)
            s += n
        }
        if s > bs {
            bs, bi = s, i + 1
        }
    }
    fmt.Printf("%d %d\n", bi, bs)
}

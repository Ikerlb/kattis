package main

import (
    "fmt"
)

func main() {
    var jon, doc string

    fmt.Scanf("%s\n", &jon)
    fmt.Scanf("%s\n", &doc)

    if len(jon) >= len(doc) {
        fmt.Println("go")
    } else {
        fmt.Println("no")
    }
}

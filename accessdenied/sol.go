package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
)

func guess(g string, l int, sc *bufio.Scanner) (bool, int) {
    fmt.Printf("%s%0*s\n", g, l - len(g), "")
    sc.Scan()

    var access string
    var ms int

    fmt.Sscanf(sc.Text(), "ACCESS %s (%d ms)", &access, &ms)

    return access == "GRANTED", ms
}

func repeat(s string, n int) string {
    var b strings.Builder
    for i := 0; i < n; i += 1 {
        b.WriteString(s)
    }
    return b.String()
}

func guessLength(sc *bufio.Scanner) (bool, int, int) {
    for l := 1; l < 21; l += 1 {
        if res, ms := guess("", l, sc); ms > 5 || res {
            return res, l, 14
        }
    }
    return false, 0, 0
}

func guessLetter(sc *bufio.Scanner, length int, prev string, prevMs int) (bool, string, int) {
    for i := 0; i < 10; i += 1 {
        c := fmt.Sprintf("%d", i)
        res, ms := guess(prev + c, length, sc)
        if res || (ms - prevMs) >= 9 {
            return res, c, prevMs + 9
        }
    }
    for i := 65; i < 91; i += 1 {
        c := string(i)
        res, ms := guess(prev + c, length, sc)
        if res || (ms - prevMs) >= 9 {
            return res, c, prevMs + 9
        }
    }
    for i := 97; i < 123; i += 1 {
        c := string(i)
        res, ms := guess(prev + c, length, sc)
        if res || (ms - prevMs) >= 9 {
            return res, c, prevMs + 9
        }
    }
    fmt.Fprintf(os.Stderr, "had to return empty string")
    return false, "", 0
}

func main() {
    var b strings.Builder
    var c string
    sc := bufio.NewScanner(os.Stdin)

    res, l, ms := guessLength(sc)
    if !res {
        for i := 0; i < l; i += 1 {
            res, c, ms = guessLetter(sc, l, b.String(), ms)
            if res {
                break
            }
            b.WriteString(c)
        }
    }
}

package main

import (
    "fmt"
    "bufio"
    "os"
)

func toInt(buf []byte) (n int64) {
    for _, v := range buf {
        n = n*10 + int64(v-'0')
    }
    return
}

type Fenwick []int64

func (f Fenwick) query(i int) int64 {
    var s int64
    s = 0
    for i > 0 {
        s += f[i]
        i -= (i & (-i))
    }
    return s
}

func (f Fenwick) update(i int, delta int64) {
    for i < len(f) {
        f[i] += delta
        i += (i & (-i))
    }
}

func parseBytes(b []byte, ft Fenwick, w *bufio.Writer) {
    var k int
    var delta int64
    if b[0] == '+' {
        prev := 2
        i := 2
        for ; i < len(b); i += 1 {
            if b[i] == ' ' {
                k = int(toInt(b[prev:i]))
                prev = i + 1
            }
        }
        if b[prev] == '-' {
            delta = -1 * toInt(b[prev + 1:])
        } else {
            delta = toInt(b[prev:])
        }
        ft.update(k + 1, delta)
    } else {
        k = int(toInt(b[2:]))
        fmt.Fprintf(w, "%d\n", ft.query(k))
    }

}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    w  := bufio.NewWriter(os.Stdout)
    defer w.Flush()

    var n, tc int
    sc.Scan()
    fmt.Sscanf(sc.Text(), "%d %d\n", &n, &tc)

    ft := Fenwick(make([]int64, n + 1))

    for i := 0; i < tc; i += 1 {

        sc.Scan()
        bytes := sc.Bytes()
        parseBytes(bytes, ft, w)

        /*if bytes[0] == '+' {
            fmt.Sscanf(line[2:], "%d %d\n", &k, &delta)
            ft.update(k + 1, delta)
        } else {
            fmt.Sscanf(line[2:], "%d\n", &k)
            fmt.Fprintf(w, "%d\n", ft.query(k))
        }*/
    }
}

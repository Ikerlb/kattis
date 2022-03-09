package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
    "strings"
    "sort"
)

type costAgency struct {
    cost int
    agency string
}

type costAgencyArr []costAgency

func (caa costAgencyArr) Len() int {
    return len(caa)
}

func (caa costAgencyArr) Swap(i, j int) {
    caa[i], caa[j] = caa[j], caa[i]
}

func (caa costAgencyArr) Less(i, j int) bool {
    if caa[i].cost < caa[j].cost {
        return true
    } else if caa[i].cost > caa[j].cost {
        return false
    } else {
        return caa[i].agency < caa[j].agency
    }
}

func min(a, b int) int {
    if a < b {
        return a
    } else {
        return b
    }
}

func solve(dp []int, a, b, n, m int) int {
    res := 0
    for n > m {
        if (n >> 1) >= m {
            ppub := float64(b) / float64(n - (n >> 1))
            if ppub <= float64(a) {
                res += b
                n = n >> 1
            } else {
                n -= 1
                res += a
            }
        } else {
            res += (n - m) * a
            break
        }
    }
    return res
}

func main() {
    w := bufio.NewWriter(os.Stdout)
    defer w.Flush()

    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()

    tc, _ := strconv.Atoi(sc.Text())
    var n, m, l, a, b int
    dp := make([]int, 100001)

    for i := 0; i < tc; i += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d %d", &n, &m, &l)
        agencies := make([]costAgency, l)
        for j := 0; j < l; j += 1 {
            sc.Scan()
            split := strings.Split(sc.Text(), ":")
            fmt.Sscanf(split[1], "%d,%d", &a, &b)
            agencies[j] = costAgency{
                cost: solve(dp, a, b, n, m),
                agency: split[0],
            }
        }
        sort.Sort(costAgencyArr(agencies))
        fmt.Fprintf(w, "Case %d\n", i + 1)
        for _, ca := range agencies {
            fmt.Fprintf(w, "%s %d\n", ca.agency, ca.cost)
        }
    }
}

package main

import (
    "fmt"
    "bufio"
    "os"
)

func kahn(g [][]int, indegree map[int]int) []string {
    res := make([]string, 0)
    q := make([]int, 0)    
    for i := 0; i < len(g); i += 1 {
        if v, _ := indegree[i]; v == 0 {
            q = append(q, i)
        }
    }

    for len(q) > 0 {
        n := q[0]
        q = q[1:]
        res = append(res, fmt.Sprintf("%d\n", n + 1))
        for _, nn := range g[n] {
            indegree[nn] -= 1 
            if indegree[nn] == 0 {
                q = append(q, nn)
            }
        }
    }
    return res
}

func main() {
    w := bufio.NewWriter(os.Stdout)
    sc := bufio.NewScanner(os.Stdin)
    var n, m, a, b int 
    sc.Scan()
    fmt.Sscanf(sc.Text(), "%d %d", &n, &m)
    
    g := make([][]int, n)
    indegree := make(map[int]int)

    for i := 0; i < m; i += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &a, &b)
        a -= 1
        b -= 1
        g[a] = append(g[a], b)
        indegree[b] += 1
    }

    res := kahn(g, indegree)
    
    if len(res) != n {
        fmt.Println("IMPOSSIBLE")
    } else {
        for i := 0; i < len(res) ; i += 1 {
            w.WriteString(res[i])
        }
        w.Flush()
    }

}

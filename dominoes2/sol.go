package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)

/*func Dfs(g map[int][]int, visited map[int]bool, node int) {
    visited[node] = true
    for _, nn := range g[node] {
        if _, e := visited[node]; e {
            Dfs(g, visited, nn)
        }
    }
}*/

func Dfs(g map[int][]int, visited map[int]bool, node int) {
    s := make([]int, 0)
    s = append(s, node)

    for len(s) > 0 {
        n := s[len(s) - 1]
        s = s[:len(s) - 1]

        visited[n] = true

        for _, nn := range g[n] {
            if _, e := visited[nn]; !e {
                s = append(s, nn)
            }
        }
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    var n, m, l, tcs, a, b int
    tcs, _ = strconv.Atoi(sc.Text())
    for tc := 0; tc < tcs; tc += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d %d", &n, &m, &l) 

        g := make(map[int][]int)
        visited := make(map[int]bool)

        for i := 0; i < m; i += 1 {
            sc.Scan()
            fmt.Sscanf(sc.Text(), "%d %d", &a, &b)
            g[a - 1] = append(g[a - 1], b - 1)
        }


        for i := 0; i < l; i += 1 {
            sc.Scan()
            node, _ := strconv.Atoi(sc.Text())
            if _, e := visited[node - 1]; !e {
                Dfs(g, visited, node - 1)
            }
        }
        fmt.Println(len(visited))
    }
}

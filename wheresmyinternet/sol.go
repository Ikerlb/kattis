package main

import (
    "fmt"
    "os"
    "bufio"
    "strings"
)

func Dfs(g map[int][]int, start, total int) []bool {
    s := make([]int, 0)
    s = append(s, start)
    visited := make([]bool, total)

    for len(s) > 0 {
        n := s[len(s) - 1]
        s = s[:len(s) - 1]
        if visited[n - 1] {
            continue            
        }
        visited[n - 1] = true
        for _, nn := range g[n] {
            s = append(s, nn)
        }
    }
    return visited 
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan() 

    var n, m, a, b int
    fmt.Sscanf(sc.Text(), "%d %d", &n, &m)

    g := make(map[int][]int)

    for i := 0; i < m; i += 1 {
        sc.Scan()
        fmt.Sscanf(sc.Text(), "%d %d", &a, &b)
        g[a] = append(g[a], b)
        g[b] = append(g[b], a)
    }

    status := Dfs(g, 1, n)    
    unvisited := make([]string, 0)
    
    for i := 0; i < n; i += 1 {
        if !status[i] {
            unvisited = append(unvisited, fmt.Sprintf("%d", i + 1))
        }
    }

    if len(unvisited) >= 1 {
        fmt.Println(strings.Join(unvisited, "\n"))
    } else {
        fmt.Println("Connected")
    }
}

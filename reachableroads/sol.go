package main

import (
    "fmt"
    "bufio"
    "os"
    "strconv"
)


/*var g map[int][]int
var visited map[int]bool*/
func Dfs(g map[int][]int, visited map[int]bool, node int) {
    visited[node] = true
    for _, nn := range g[node] {
        if _, e := visited[nn]; !e {
            Dfs(g, visited, nn)
        }
    }
}

func main() {
    var a, b int
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    cities, _ := strconv.Atoi(sc.Text())

    for c := 0; c < cities; c += 1 {
        sc.Scan()
        n, _ := strconv.Atoi(sc.Text())    
        sc.Scan()
        m, _ := strconv.Atoi(sc.Text())    

        visited := make(map[int]bool)
        g := make(map[int][]int)
        
        for i := 0; i < m; i += 1 {
            sc.Scan()
            fmt.Sscanf(sc.Text(), "%d %d", &a, &b)
            g[a] = append(g[a], b) 
            g[b] = append(g[b], a) 
        }
        cc := 0
        for i := 0; i < n; i += 1 {
            if _, e := visited[i]; !e {
                Dfs(g, visited, i)
                cc += 1
            }
        }
        fmt.Println(cc - 1)
    }
    
}

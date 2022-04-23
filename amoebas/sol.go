package main

import (
    "fmt"
    "bufio"
    "os"
)

type RowCol struct {
    Row, Col int;
}

func ParseLine(s string) []int {
    res := make([]int, len(s))
    for i, c := range s {
        if string(c) == "#" {
            res[i] = 2
        } else {
            res[i] = 1
        }
    }
    return res
}

func Dfs(grid [][]int, sr, sc int) {
    var rc RowCol
    s := make([]RowCol, 0)
    s = append(s, RowCol{sr, sc})

    for len(s) > 0 {
        rc, s = s[len(s) - 1], s[:len(s) - 1]
        r := rc.Row
        c := rc.Col
        grid[r][c] = -2
        for dr := -1; dr < 2; dr += 1 {
            for dc := -1; dc < 2; dc += 1 {
                if dr == 0 && dc == 0{
                    continue    
                } else if (r + dr) < 0 || (r + dr) >= len(grid) {
                    continue
                } else if (c + dc) < 0 || (c + dc) >= len(grid[0]) {
                    continue
                } else if grid[r + dr][c + dc] != 2 {
                    continue        
                } else {
                    s = append(s, RowCol{r + dr, c + dc})
                }
            }
        }
    }
}

func main() {
    var n, m int        
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    fmt.Sscanf(sc.Text(), "%d %d", &n, &m)

    grid := make([][]int, n) 
    for r := 0; r < n; r += 1 {
        sc.Scan()
        grid[r] = ParseLine(sc.Text())
    }

    cc := 0
    for r := 0; r < n; r += 1 {
        for c := 0; c < m; c += 1 {
            if grid[r][c] == 2 {
                Dfs(grid, r, c)
                cc += 1
            }
        }
    }
    fmt.Printf("%d\n", cc)
}

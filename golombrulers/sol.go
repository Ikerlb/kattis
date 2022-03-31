package main

import (
    "fmt"
    "bufio"
    "os"
    "strings"
    "strconv"
    "sort"
)

func isGolomb(arr []int) string {
    m := make(map[int]int)
    for i := 0; i < len(arr); i += 1{
        for j := i + 1; j < len(arr); j += 1 {
            m[arr[j] - arr[i]] += 1
        }
    }
    missing := make([]string, 0)
    for i := 1; i < arr[len(arr) - 1]; i += 1 {
        if v, e := m[i]; e && v > 1 {
            return "not a ruler"
        } else if !e {
            missing = append(missing, fmt.Sprintf("%d", i))
        }
    }
    if len(missing) == 0 {
        return "perfect"
    } else {
        ms := strings.Join(missing, " ")
        return fmt.Sprintf("missing %s", ms)
    }
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    
    for sc.Scan() {
        arr := make([]int, 0)
        for _, s := range strings.Split(sc.Text(), " ") {
            n, _ := strconv.Atoi(s)
            arr = append(arr, n)
        }
        sort.Ints(arr)
        fmt.Println(isGolomb(arr))
    }
}

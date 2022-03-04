package main

import (
    "fmt"
    "sort"
    "strings"
    "bufio"
    "os"
    "strconv"
)



func parseLine(sc *bufio.Scanner) string {
    var c, n string
    sc.Scan()
    fmt.Sscanf(sc.Text(), "%s %s class\n", &n, &c)

    classS := strings.Split(c, "-")
    class := [10]rune{'1','1','1','1','1','1','1','1','1','1'}
    j := 0
    for i := (len(classS) - 1); i >= 0; i -= 1{
        switch classS[i] {
        case "upper":
            class[j] = '0'
        case "middle":
            class[j] = '1'
        default:
            class[j] = '2'
        }
        j += 1
    }

    return fmt.Sprintf("%s %s", string(class[:]), n[0:len(n) - 1])
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    tc, _ := strconv.Atoi(sc.Text())

    for t := 0; t < tc; t += 1 {
        sc.Scan()
        n, _ := strconv.Atoi(sc.Text())
        arr := make([]string, n)
        for i := 0; i < n; i += 1 {
            arr[i] = parseLine(sc)
        }

        sort.Strings(arr)
        for _, n := range arr {
           fmt.Printf("%s\n", n[11:])
        }
       fmt.Printf("==============================\n")
    }

}

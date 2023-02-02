package main

import (
    "bufio"
    "strconv"
    "fmt"
    "os"
)

func getFromContext(c []map[string]string, iden string) (bool, string) {
    for i := len(c) - 1; i >= 0; i -= 1 {
        if k, e := c[i][iden]; e {
            return true, k
        }
    }
    return false, ""
}

func main() {
    sc := bufio.NewScanner(os.Stdin)
    sc.Split(bufio.ScanWords)
    sc.Scan()
    n, _ := strconv.Atoi(sc.Text())

    context := make([]map[string]string, 1)
    context[0] = make(map[string]string)

    for i := 0; i < n; i += 1 {
        sc.Scan()
        tok := sc.Text()
        //fmt.Println(tok, i)
        if tok == "{" {
            context = append(context, make(map[string]string))
        } else if tok == "}" {
            context = context[:len(context) - 1]
        } else if tok == "DECLARE" {
            sc.Scan()
            iden := sc.Text()
            sc.Scan()
            typ := sc.Text()
            _, e := context[len(context) - 1][iden]
            if e {
                fmt.Println("MULTIPLE DECLARATION")
                os.Exit(0)
            } else {
                context[len(context) - 1][iden] = typ
            }
        } else if tok == "TYPEOF" {
            sc.Scan()
            iden := sc.Text()
            e, s := getFromContext(context, iden)
            if e {
                fmt.Println(s)
            } else {
                fmt.Println("UNDECLARED")
            }
        }
    }
}

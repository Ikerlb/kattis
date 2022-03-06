package main

import (
    "fmt"
    "os"
    "bufio"
    "strconv"
    "strings"
)

type Operator struct {
    Function func(int, int)int
    Precedence int
}

func add(x, y int) int {return x + y}
func div(x, y int) int {
    if y == 0 {
        return int(^uint(0) >> 1)
    } else {
        return int(x / y)
    }
}
func mult(x, y int) int {return x * y}
func sub(x, y int) int {return x - y}

var operators map[string]Operator = map[string]Operator{
    "+": Operator{add, 0},
    "-": Operator{sub, 0},
    "*": Operator{mult, 1},
    "/": Operator{div, 1},
}

// https://rosettacode.org/wiki/Parsing/Shunting-yard_algorithm#Go
func shuntingYard(tokens []string) []string {
    nums := make([]string, 0)
    ops := make([]string, 0)
    for _, c := range tokens {
        //fmt.Printf("nums: %v ops: %v\n", nums, ops)
        if o1, isOp := operators[c]; isOp {
            for len(ops) > 0 {
                v := ops[len(ops) - 1]
                o2, isOp := operators[v]
                if !isOp || o1.Precedence > o2.Precedence{
                    break
                }
                ops = ops[:len(ops) - 1]
                nums = append(nums, v)
            }
            ops = append(ops, c)
        } else {
            nums = append(nums, c)
        }
    }

    for i := (len(ops) - 1); i >= 0; i -= 1 {
        nums = append(nums, ops[i])
    }

    return nums
}

func product(a ...[]string) (c [][]string) {
    if len(a) == 0 {
        return [][]string{nil}
    }
    r := product(a[1:]...)
    for _, e := range a[0] {
        for _, p := range r {
            c = append(c, append([]string{e}, p...))
        }
    }
    return
}

func formatExpression(permutation []string, val int) []string{
    res := make([]string, 1 + 2 * len(permutation))
    strVal := fmt.Sprintf("%d", val)
    for i := 0; i < len(permutation); i += 1 {
        res[2 * i] = strVal
        res[2 * i + 1] = permutation[i]
    }
    res[len(res) - 1] = strVal
    return res
}

func eval(rpn []string) int {
    res := make([]int, 0)
    var v1, v2, v3 int
    for _, c := range rpn {
        if strings.Contains("+-*/", c) {
            res, v2 = res[0:len(res) - 1], res[len(res) - 1]
            res, v1 = res[0:len(res) - 1], res[len(res) - 1]
            v3 = operators[c].Function(v1, v2)
            res = append(res, v3)
        } else {
            n, _ := strconv.Atoi(c)
            res = append(res, n)
        }
    }
    return res[0]
}

func main() {

    results := make(map[int]string, 0)


    ops := []string{"+","*","/","-"}
    for _, poss := range product(ops, ops, ops) {
        formatted := formatExpression(poss, 4)
        rpn := shuntingYard(formatted)
        r := eval(rpn)
        //fmt.Printf("expr: %v -> rpn: %v -> %v\n", formatted, rpn, r)
        results[r] = fmt.Sprintf("%s = %d", strings.Join(formatted, " "),r)
        //fmt.Printf("%s = %d\n", strings.Join(formatted, " "),r)
    }

    sc := bufio.NewScanner(os.Stdin)
    sc.Scan()
    k, _ := strconv.Atoi(sc.Text())

    for i := 0; i < k; i += 1 {
        sc.Scan()
        n, _ := strconv.Atoi(sc.Text())

        if r, exists := results[n]; exists {
            fmt.Printf("%s\n", r)
        } else {
            fmt.Println("no solution")
        }

    }
}

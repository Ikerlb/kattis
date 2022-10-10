package main

import (
    "os"
    "fmt"
    "bufio"
    "strconv"
    "strings"
)

func Min(nums ...int) int {
    if len(nums) == 1 {
        return nums[0]
    } else {
        res := nums[0]
        for i := 1; i < len(nums); i += 1 {
            if nums[i] < res {
                res = nums[i]
            }
        }
        return res
    }
}

func nextLesser(nums []int, reverse bool) []int {
    res := make([]int, len(nums))
    for i := 0; i < len(nums); i += 1 {
        res[i] = -1
    }
    var j int
    s := make([]int, 0)
    if reverse {
        for i := 0; i < len(nums); i += 1 {
            for len(s) > 0 && (nums[i] > nums[s[len(s) - 1]]) {
                //fmt.Printf("%v %v\n", res, s)
                j, s = s[len(s) - 1], s[:len(s) - 1]
                res[j] = i
            }
            s = append(s, i)
        }
    } else {
        for i := len(nums) - 1; i >= 0; i -= 1 {
            for len(s) > 0 && (nums[i] > nums[s[len(s) - 1]]) {
                //fmt.Printf("%v %v\n", res, s)
                j, s = s[len(s) - 1], s[:len(s) - 1]
                res[j] = i
            }
            s = append(s, i)
        }
    }
    return res
}

func dp(i int, heights []int, n2l []int, n2r []int, cache map[int]int) int {
    if v, ok := cache[i]; ok {
        return v
    }
    const MaxInt = int((^uint(0)) >> 1) 
    if n2l[i] == -1 && n2r[i] == -1 {
        cache[i] = 0;
        return 0
    }
    res := MaxInt
    if n2l[i] != -1 {
        res = Min(res, dp(n2l[i], heights, n2l, n2r, cache) + 1)
    }
    if n2r[i] != -1 {
        res = Min(res, dp(n2r[i], heights, n2l, n2r, cache) + 1)
    }
    cache[i] = res;
    return res
}

func main() {
    sc :=  bufio.NewScanner(os.Stdin)
    sc.Scan()
    n, _ := strconv.Atoi(sc.Text())
    //fmt.Println(n)

    heights := make([]int, n)

    cache := make(map[int]int)

    for i := 0; i < n; i += 1 {
        sc.Scan()
        h, _ := strconv.Atoi(sc.Text()) 
        heights[i] = h
    }

    //fmt.Printf("%v\n", heights)
    n2r := nextLesser(heights, false)
    //fmt.Printf("n2r %v\n", n2r)
    n2l := nextLesser(heights, true)
    //fmt.Printf("n2l  %v\n", n2l)

    res := make([]string, n)
    for i := 0; i < n; i += 1 {
        res[i] = fmt.Sprintf("%d", dp(i, heights, n2l, n2r, cache))
    }
    fmt.Println(strings.Join(res, " "))
}

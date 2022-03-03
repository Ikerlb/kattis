package main

import (
    "fmt"
    "sort"
    "strings"
    "os"
    "bufio"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }

func twoSum(arr []int, target int) {
    i := 0
    j := len(arr) - 1

    for i < j {
        if arr[i] + arr[j] == target {
            printf("Yes\n")
            return
        } else if arr[i] + arr[j] < target {
            i += 1
        } else {
            j -= 1
        }
    }
    printf("No\n")
}

func unique(arr []int) {
    prev := -1
    for _, n := range arr {
        if prev == n {
            printf("Contains duplicate\n")
            return
        } else {
            prev = n
        }
    }
    printf("Unique\n");
}

func findMode(arr []int) {
    half := len(arr) >> 1
    if arr[0] == arr[half] {
        printf("%d\n", arr[0])
    } else {
        printf("-1\n")
    }
}

func findMedian(arr []int) {
    half := len(arr) >> 1
    if len(arr) & 1 == 0 { // even
        printf("%d %d\n", arr[half - 1], arr[half])
    } else {
        printf("%d\n", arr[half])
    }
}

func printInRange(arr []int, lo, hi int) {
    res := make([]string, 0)
    for _, n := range arr {
        if n >= lo && n <= hi {
            res = append(res, fmt.Sprintf("%d", n))
        }
    }
    printf("%s\n", strings.Join(res, " "))
}

func main() {
    defer writer.Flush()

    var n, t int;

    scanf("%d %d\n", &n, &t)
    //printf("%d %d\n", n, t)

    arr := make([]int, n)

    for i := 0; i < n; i += 1 {
        scanf("%d", &arr[i])
    }

    //printf("%v\n", arr)

    sort.Ints(arr)

    switch t {
    case 1:
        twoSum(arr, 7777)
    case 2:
        unique(arr)
    case 3:
        findMode(arr)
    case 4:
        findMedian(arr)
    case 5:
        printInRange(arr, 100, 999)
    default:
        printf("default\n")
    }
}

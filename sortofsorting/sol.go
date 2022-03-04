package main

import (
    "fmt"
    "sort"
    "os"
    "bufio"
    "strings"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

func printf(f string, a ...interface{}) {
    fmt.Fprintf(writer, f, a...)
}

func scanf(f string, a ...interface{}) {
    fmt.Fscanf(reader, f, a...)
}

type ByOther []string

func (a ByOther) Len() int           { return len(a) }
func (a ByOther) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a ByOther) Less(i, j int) bool { return a[i][0:2] < a[j][0:2] }

func main() {
    defer writer.Flush()

    var n int;
    i := 0
    for scanf("%d\n", &n); n > 0; scanf("%d\n", &n){
        if i > 0 {
            printf("\n")
        }
        arr := make([]string, n)
        for i := 0; i < n; i += 1 {
            scanf("%s\n", &arr[i])
        }
        sort.Stable(ByOther(arr))
        printf("%s\n", strings.Join(arr, "\n"))
        i += 1
    }
}

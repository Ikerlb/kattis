package main

import (
    "fmt"
    "bufio"
    "os"
)

var reader *bufio.Reader = bufio.NewReader(os.Stdin)
var writer *bufio.Writer = bufio.NewWriter(os.Stdout)
func printf(f string, a ...interface{}) { fmt.Fprintf(writer, f, a...) }
func scanf(f string, a ...interface{}) { fmt.Fscanf(reader, f, a...) }

type RowCol struct {
    Row, Col int;
}

func (rc *RowCol) flatten(cols int) int {
    return rc.Row * cols + rc.Col
}

type UnionFind struct {
	root []int
	size []int
}

// New returns an initialized list of size
func New(size int) *UnionFind {
	return new(UnionFind).init(size)
}

// Constructor initializes root and size arrays
func (uf *UnionFind) init(size int) *UnionFind {
	uf = new(UnionFind)
	uf.root = make([]int, size)
	uf.size = make([]int, size)

	for i := 0; i < size; i++ {
		uf.root[i] = i
		uf.size[i] = 1
	}

	return uf
}

// Union connects p and q by finding their roots and comparing their respective
// size arrays to keep the tree flat
func (uf *UnionFind) Union(p int, q int) {
	qRoot := uf.Root(q)
	pRoot := uf.Root(p)

	if uf.size[qRoot] < uf.size[pRoot] {
		uf.root[qRoot] = uf.root[pRoot]
		uf.size[pRoot] += uf.size[qRoot]
	} else {
		uf.root[pRoot] = uf.root[qRoot]
		uf.size[qRoot] += uf.size[pRoot]
	}
}

// Root or Find traverses each parent element while compressing the
// levels to find the root element of p
// If we attempt to access an element outside the array it returns -1
func (uf *UnionFind) Root(p int) int {
	if p > len(uf.root)-1 {
		return -1
	}

	for uf.root[p] != p {
		uf.root[p] = uf.root[uf.root[p]]
		p = uf.root[p]
	}

	return p
}

// Root or Find
func (uf *UnionFind) Find(p int) int {
	return uf.Root(p)
}

// Check if items p,q are connected
func (uf *UnionFind) Connected(p int, q int) bool {
	return uf.Root(p) == uf.Root(q)
}

func neighbors(rc RowCol) []RowCol {
    deltas := []RowCol{RowCol{0, 1}, RowCol{1, 0}, RowCol{-1, 0}, RowCol{0, -1}}
    nn := make([]RowCol, 0, 4)
    for _, drc := range deltas {
        nn = append(nn, RowCol{rc.Row + drc.Row, rc.Col + drc.Col})
    }
    return nn
}

func inBounds(grid [][]int, rc RowCol) bool {
    return rc.Row >= 0 && rc.Row < len(grid) && rc.Col >= 0 && rc.Col < len(grid[0])
}

func floodfill(grid [][]int, r, c, val int, ufs *UnionFind) {
    var rc RowCol;
    s := make([]RowCol, 0, 1)
    s = append(s, RowCol{r, c})

    cols := len(grid[0])

    for len(s) > 0 {
        rc, s = s[len(s)-1], s[:len(s)-1]
        grid[rc.Row][rc.Col] *= -1
        for _, nrc := range neighbors(rc) {
            if inBounds(grid, nrc)  && grid[nrc.Row][nrc.Col] == val{
                ufs.Union(rc.flatten(cols), nrc.flatten(cols))
                s = append(s, nrc)
            }
        }
    }
}

func Abs(x int) int {
    if x < 0 {
        return -x
    } else {
        return x
    }
}

func main() {
    defer writer.Flush()

    var rows, cols int
    scanf("%d %d\n", &rows, &cols)

    grid := make([][]int, 0, rows)
    for r := 0; r < rows; r += 1 {
        var sRow string;
        row := make([]int, 0, cols)
        scanf("%s\n", &sRow)

        for _, r := range sRow {
            row = append(row, int(r - '0') + 1)
        }

        grid = append(grid, row)
    }

    uf := New(rows * cols)
    for r := 0; r < rows; r += 1 {
        for c := 0; c < cols; c += 1 {
            if grid[r][c] > 0 {
                floodfill(grid, r, c, grid[r][c], uf)
            }
        }
    }

    var queries int;
    scanf("%d\n", &queries)


    for q := 0; q < queries; q += 1 {
        var r1, r2, c1, c2 int
        scanf("%d %d %d %d\n", &r1, &c1, &r2, &c2)

        rc1 := RowCol{r1 - 1, c1 - 1}
        rc2 := RowCol{r2 - 1, c2 - 1}

        if uf.Connected(rc1.flatten(cols), rc2.flatten(cols)) {
            if Abs(grid[rc1.Row][rc1.Col]) == 2 {
                printf("decimal\n")
            } else {
                printf("binary\n")
            }
        } else {
            printf("neither\n")
        }
    }
}

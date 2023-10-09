def rotate_90(grid):
    return [list(reversed(col)) for col in zip(*grid)]

# get kth diagonal
def get_diagonals(grid, k):
    n, m = len(grid), len(grid[0])
    for i in reversed(range(n)):
        if 0 <= k - i < m:
            yield i, k - i

def format_45(grid):
    n, m = len(grid), len(grid[0])
    res = []
    for i in range(n):
        row = []
        row.append(" " * (n - i - 1))
        row.append(" ".join(grid[r][c] for r, c in get_diagonals(grid, i)))
        res.append("".join(row))
    for i in range(m - 1):
        row = []
        row.append(" " * (i + 1))
        row.append(" ".join(grid[r][c] for r,c in get_diagonals(grid,n+i)))
        res.append("".join(row))
    return "\n".join(res)
    

def format(grid):
    res = []
    for row in grid:
        res.append("".join(row))
    return "\n".join(res)


n, m = map(int, input().split(" "))

grid = []
for _ in range(n):
    grid.append(list(input()))

k = int(input()) % 360

while k >= 90:
    grid = rotate_90(grid)
    k -= 90

if k == 45:
    print(format_45(grid))
else:
    print(format(grid))

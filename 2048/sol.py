from itertools import groupby, repeat

grid = []
for i in range(4):
    line = input()
    grid.append([int(n) for n in line.split(" ")])

move = int(input())

# mutates grid
def _rotate(grid, level):
    s, e = level, len(grid) - 1 - level

    for i in range(e - s):
        aux = grid[s][s+i]    
        grid[s][s+i] = grid[s+i][e]
        grid[s+i][e] = grid[e][e-i]
        grid[e][e-i] = grid[e-i][s]
        grid[e-i][s] = aux

# mutates grid
def rotate(grid):
    for l in range(len(grid) // 2):
        _rotate(grid, l)    
    return grid

def step(grid, move):
    ngrid = [row[:] for row in grid]
    for _ in range(move):
        rotate(ngrid)
    res = []
    for row in ngrid:
        nrow = []
        for k, g in groupby(e for e in row if e != 0):
            d, m = divmod(len(list(g)), 2)
            nrow.extend(repeat(k + k, d))
            nrow.extend(repeat(k, m))
        nrow.extend(0 for i in range(len(row) - len(nrow)))
        res.append(nrow) 
    for _ in range((4 - move) % 4):
        rotate(res)
    return res

ngrid = step(grid, move)

for row in ngrid:
   print(" ".join(map(str, row)))

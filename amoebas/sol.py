from itertools import product

n, m = map(int, input().split(" "))

grid = [[int(c == "#") + 1 for c in input()] for _ in range(n)]

def neighbors(grid, r, c):
    g = product([0, -1, 1], repeat = 2)
    next(g)
    for dr, dc in g:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):        
            yield r + dr, c + dc

def dfs(grid, r, c):
    grid[r][c] = -grid[r][c]
    for nr, nc in neighbors(grid, r, c):
        if grid[nr][nc] > 0 and grid[nr][nc] == abs(grid[r][c]):
            dfs(grid, nr, nc)

cc = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] == 2:
            dfs(grid, r, c)
            cc += 1       
print(cc)

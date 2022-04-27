m, n = map(int, input().split(" "))

def neighbors(grid, r, c):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            yield r + dr, c + dc 

def fmt(grid):
    res = []
    for row in grid:
        res.append("".join(c if c is not None else "$" for c in row))
    return "\n".join(res)
            

def dfs(grid, r, c):
    if grid[r][c] is None or grid[r][c] == "#":
        return 0    
    res = int(grid[r][c] == "G")
    grid[r][c] = None
    for nr, nc in neighbors(grid, r, c):
        res += dfs(grid, nr, nc)        
    return res

grid = [list(input()) for _ in range(n)]
print(fmt(grid))
print()
sr = sc = None
for r in range(n):
    for c in range(m):
        if grid[r][c] == "P":
            sr, sc = r, c
        elif grid[r][c] == "T":
            grid[r][c] == "#"    
            for nr, nc in neighbors(grid, r, c):
                grid[nr][nc] = "#"

print(fmt(grid))
print(dfs(grid, sr, sc))

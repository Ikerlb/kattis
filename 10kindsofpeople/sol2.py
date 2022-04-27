n, m = map(int, input().split(" "))

grid = [[int(c) + 1 for c in input()] for _ in range(n)]

def fmt(grid):
    return "\n".join("".join(map(lambda x: str(x).rjust(2), row)) for row in grid)

def neighbors(grid, r, c):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            yield r + dr, c + dc

def dfs(grid, sr, sc, d, cc):
    d[cc] = grid[sr][sc]
    s = [(sr, sc)]
    while s:
        r, c = s.pop()
        v, grid[r][c] = grid[r][c], -cc
        for nr, nc in neighbors(grid, r, c):
            if grid[nr][nc] > 0 and grid[nr][nc] == v:
                s.append((nr, nc))


#print(fmt(grid))
d, cc = {}, 0
for r in range(n):
    for c in range(m):
        if grid[r][c] > 0:
            dfs(grid, r, c, d, cc)    
            cc += 1
#print(fmt(grid))

qs = int(input())
for q in range(qs):
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split(" "))
    if grid[r1][c1] != grid[r2][c2]:
        print("neither")
    elif d[abs(grid[r1][c1])] == 1:
        print("binary")
    else:
        print("decimal")

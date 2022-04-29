n, m = map(int, input().split(" "))
grid = [[1 for _ in range(m + 2)]]
for _ in range(n):
    grid.append([1] + [int(c) + 1 for c in input()] + [1])
grid.append([1 for _ in range(m + 2)])

def fmt(grid):
    res = []
    for row in grid:
        res.append("".join(map(lambda x: str(x).rjust(3), row)))    
    return "\n".join(res)

def neighbors(grid, r, c):
    for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
            yield r + dr, c + dc

def floodfill(grid, sr, sc):
    s = [(sr, sc)]
    res = 0
    while s:
        r, c = s.pop()
        for nr, nc in neighbors(grid, r, c):
            if grid[nr][nc] > 0 and -grid[nr][nc] == grid[r][c]:
                grid[nr][nc] = -grid[nr][nc]
                s.append((nr, nc))
            elif grid[nr][nc] > 0:
                res += 1
    return res

#print(fmt(grid))
grid[0][0] = -1
print(floodfill(grid, 0, 0))
#print(fmt(grid))

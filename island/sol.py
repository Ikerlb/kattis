from sys import stdin

def floodfill(g, r, c, a, v):
    s = [(r, c)]
    while s:
        r, c = s.pop()
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if not 0 <= r + dr < len(g):
                continue
            if not 0 <= c + dc < len(g[0]):
                continue
            if (r + dr, c + dc) in v:
                continue    
            if g[r + dr][c + dc] not in a:
                continue
            nr, nc = r + dr, c + dc
            v.add((nr, nc))
            s.append((nr, nc))

def dfs(grid, allow):
    visited = set()
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] in allow:
                visited.add((r, c))
                floodfill(grid, r, c, allow, visited)
                res += 1
    return res

def floodfill2(g, r, c, v):
    s = [(r, c)]
    while s:
        r, c = s.pop()
        if grid[r][c] == "X":
            allow = "BX#"
        elif grid[r][c] == "B":
            allow = "BX"
        else:
            allow = "X#"
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if not 0 <= r + dr < len(g):
                continue
            if not 0 <= c + dc < len(g[0]):
                continue
            if (r + dr, c + dc) in v:
                continue    
            if grid[r + dr][c + dc] not in allow:
                continue    
            nr, nc = r + dr, c + dc
            #if allow == "BX#":
            #    print(nr, nc)
            v.add((nr, nc))
            s.append((nr, nc))

def buses_needed(grid):
    visited = set()
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in visited and grid[r][c] in "#X":
                res += 1
                visited.add((r, c))
                floodfill2(grid, r, c, visited)
    return res

def _fmt(grid):
    return "\n".join("".join(row) for row in grid)

def solve(grid, m):
    res = []
    bridges = dfs(grid, "B")  # not sure this works
    islands = dfs(grid, "#X") # this does work
    buses = buses_needed(grid)
    res.append(f"Map {m}") 
    res.append(f"islands: {islands}")
    res.append(f"bridges: {bridges}")
    res.append(f"buses needed: {buses}")
    return "\n".join(res)

m = 1
grid = []
res = []
for line in stdin:
    line = line[:-1]
    if not line:
        res.append(solve(grid, m))
        m += 1
        grid = []
        continue 
    grid.append(list(line))   
res.append(solve(grid, m))
print("\n\n".join(res))

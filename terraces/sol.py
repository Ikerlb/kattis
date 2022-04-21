from collections import defaultdict

def neighbors(grid, r, c):
    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if not 0 <= r + dr < len(grid):
            continue
        if not 0 <= c + dc < len(grid[0]):
            continue
        yield r + dr, c + dc

def floodfill(grid, by_cc, by_coord, sr, sc, cc):
    s = [(sr, sc)]
    while s:
        r, c = s.pop()
        by_cc[cc].append((r, c))
        by_coord[(r, c)] = cc
        for nr, nc in neighbors(grid, r, c):    
            if grid[nr][nc] > 0 and abs(grid[nr][nc]) == abs(grid[r][c]):
                grid[nr][nc] = -grid[nr][nc]
                s.append((nr, nc))

m, n = map(int, input().split(" "))
grid = [[int(s) + 1 for s in input().split(" ")] for _ in range(n)]
by_cc = defaultdict(list)
by_coord = defaultdict(int)

cc = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] > 0:
            grid[r][c] = -grid[r][c]
            floodfill(grid, by_cc, by_coord, r, c, cc)
            cc += 1

g = defaultdict()

def create_graph(grid, by_cc, by_coord):
    g = defaultdict(set)
    for cc in by_cc.keys():
        g[cc].update(by_coord[n] for r, c in by_cc[cc] for n in neighbors(grid, r, c))
        g[cc].discard(cc)
    return g 
            
                        
def format_by_cc(grid, by_coord):
    res = []
    for r in range(len(grid)):
        res.append(" ".join(str(by_coord[(r, c)]) for c in range(len(grid[0]))))
    return "\n".join(res)

def can_flow_downwards(g, grid, by_cc, by_coord, cc):
    #assert(len(by_cc[cc]) > 0)
    r, c = by_cc[cc][0]
    for nn in g[cc]:
        # there MUST be at least one
        #assert(len(by_cc[nn]) > 0)
        nr, nc = by_cc[nn][0]
        if abs(grid[nr][nc]) < abs(grid[r][c]):
            return True
    return False



g = create_graph(grid, by_cc, by_coord)
res = 0
for cc in by_cc.keys():
    if not can_flow_downwards(g, grid, by_cc, by_coord, cc):
        res += len(by_cc[cc])
print(res)

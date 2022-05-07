from collections import deque

tcs = int(input())

def fmt(grid):
    return "\n".join("".join(row) for row in grid)

def neighbors(grid, r, c):
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        
            yield r + dr, c + dc, 

def solve(grid, sr, sc, fires):
    s = deque([(sr, sc)])
    turns = 0
    while s:
        for _ in range(len(s)):
            r, c = s.popleft()
            if grid[r][c] == "*":
                continue
            for nr, nc in neighbors(grid, r, c):
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                    return turns + 1
                elif grid[nr][nc] == ".":
                    grid[nr][nc] = "@"
                    s.append((nr, nc))
        for _ in range(len(fires)):
            r, c = fires.popleft()
            for nr, nc in neighbors(grid, r, c):
                if not 0 <= nr < len(grid) or not 0 <= nc < len(grid[0]):
                    continue
                if grid[nr][nc] not in "#*":
                    grid[nr][nc] = "*"
                    fires.append((nr, nc))
        turns += 1
    return None

for _ in range(tcs):
    m, n = map(int, input().split(" "))
    grid = []
    fires = deque()
    for r in range(n):
        grid.append([])
        for c, ch in enumerate(input()):
            grid[-1].append(ch)
            if ch == "*":
                fires.append((r, c))
            elif ch == "@":
                sr, sc = r, c
    #print(fires)
    #print(sr, sc)
    #print(fmt(grid))
    res = solve(grid, sr, sc, fires)
    if res is None:
        print("IMPOSSIBLE")
    else:
        print(res)

# ###.###
# #*#.#*#
# #.....#
# #.....#
# #..@..#
# #######

# ###.###
# #*#.#*#
# #*...*#
# #..@..#
# #.@.@.#
# #######

# ###.###
# #*#.#*#
# #**@**#
# #*@.@*#
# #@...@#
# #######

# ###.###
# #*#@#*#
# #*****#
# #**.**#
# #*...*#
# #######

# ###@###
# #*#*#*#
# #*****#
# #*****#
# #**.**#
# #######

#    @
# ###*###
# #*#*#*#
# #*****#
# #*****#
# #*****#
# #######

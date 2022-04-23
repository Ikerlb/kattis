tc = 1
while True:
    try:
        n, m = map(int, input().split(" "))
    except:
        break

    def neighbors(grid, r, c):
        for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            if 0 <= r + dr < len(grid) and 0 <= c + dc < len(grid[0]):
                yield r + dr, c + dc

    def dfs(grid, sr, sc):
        s = [(sr, sc)]
        while s:
            r, c = s.pop()
            grid[r][c] = -1
            for nr, nc in neighbors(grid, r, c):
                if grid[nr][nc] == 1:
                    s.append((nr, nc)) 

    grid = [[int(c == "#") + 1 for c in input()] for _ in range(n)]

    cc = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                dfs(grid, r, c)
                cc += 1
    print(f"Case {tc}: {cc}")
    tc += 1

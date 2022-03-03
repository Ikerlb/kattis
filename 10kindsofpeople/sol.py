class UFS:
    def __init__(self, n):
        self.parents = [i for i in range(n)]    
    
    def _root(self, n):
        if self.parents[n] == n:                 
            return n
        self.parents[n] = self._root(self.parents[n])
        return self.parents[n]

    def same(self, a, b):
        ra = self._root(a)
        rb = self._root(b)
        return ra == rb

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return False

        self.parents[ra] = rb
        return True

    def find(self, a):
        return self._root(a)

    def __repr__(self):
        return f"{self.parents}"

def f(grid, r, c):
    return r * len(grid[0]) + c

def in_bounds(grid, r, c):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def floodfill(grid, r, c, ufs, val):
    s = [(r, c)]
    while s:
        r, c = s.pop() 
        grid[r][c] = -grid[r][c]
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if in_bounds(grid, r + dr, c + dc) and grid[r+dr][c+dc] == val:
                ufs.union(f(grid, r, c), f(grid, r + dr, c + dc))
                s.append((r + dr, c + dc))

def solve(grid, queries):
    ufs = UFS(len(grid) * len(grid[0]))
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] > 0:
                floodfill(grid, r, c, ufs, grid[r][c])

    for r1, c1, r2, c2 in queries:
        if ufs.same(f(grid, r1, c1), f(grid, r2, c2)):
            print("decimal" if abs(grid[r1][c1]) == 2 else "binary")
        else:
            print("neither")

r, _ = map(int, input().split(" "))
grid = []
for _ in range(r):
    grid.append([int(n) + 1 for n in input()])

queries = []
qs = int(input())
for _ in range(qs):
    queries.append([int(n) - 1 for n in input().split(" ")])

solve(grid, queries)

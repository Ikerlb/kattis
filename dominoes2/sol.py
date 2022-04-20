from collections import defaultdict

tcs = int(input())

def dfs(g, visited, node):
    visited.add(node)
    for nn in g[node]:
        if nn not in visited:
            dfs(g, visited, nn)

for _ in range(tcs):
    n, m, l = map(int, input().split(" "))
    visited = set()
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split(" "))
        g[a - 1].append(b - 1)
    for _ in range(l):
        node = int(input()) - 1
        dfs(g, visited, node)
    print(len(visited))
    #print(visited)


from collections import defaultdict

def dfs(g, visited, node):
    visited.add(node)
    for nn in g[node]:    
        if nn not in visited:
            dfs(g, visited, nn)

cities = int(input())
for _ in range(cities):
    n = int(input())
    m = int(input())
    g = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split(" "))
        g[a].append(b)
        g[b].append(a)
    visited = set()
    cc = 0
    for i in range(n): 
        if i not in visited:
            dfs(g, visited, i)
            cc += 1
    print(cc - 1)

from collections import defaultdict

g = defaultdict(list)

n, m = map(int, input().split(" "))

for _ in range(m):
    a, b = map(int, input().split(" "))
    g[a].append(b)
    g[b].append(a)


def dfs(g, src, n):
    s = [src]
    visited = set(range(1, n + 1))
    while s:
        n = s.pop()
        if n not in visited:
            continue
        visited.discard(n)
        for nn in g[n]:
            s.append(nn)
    return visited
            
        
s = dfs(g, 1, n)
if s:
    print("\n".join(map(str, sorted(s))))
else:
    print("Connected")

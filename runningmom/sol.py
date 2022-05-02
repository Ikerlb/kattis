import traceback
from collections import defaultdict

n = int(input())

g = defaultdict(list)
visited = {}

for _ in range(n):
    o, d = input().split(" ")
    g[o].append(d)
    visited[o] = 0
    visited[d] = 0


# cycle detection with dfs
def dfs(g, visited, n):
    visited[n] = 1
    for nn in g[n]:
        if visited[nn] == 0:
            if not dfs(g, visited, nn):
                return False
        elif visited[nn] == 1:
            return False
    visited[n] = 2
    return True

while True:
    try:
        city = input()
        for k in visited:
            visited[k] = 0    
        if dfs(g, visited, city):
            print(f"{city} trapped")
        else:
            print(f"{city} safe")
    except:
        break

from collections import defaultdict, deque

n, m = map(int, input().split(" "))

g = defaultdict(list)
indegree = defaultdict(int)

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split(" "))
    g[a].append(b)
    indegree[b] += 1

def kahn(nodes, g, indegree):
    q = deque(i for i in range(nodes) if indegree[i] == 0)
    res = []
    while q:
        n = q.popleft()    
        res.append(str(n + 1))
        for nn in g[n]:
            indegree[nn] -= 1        
            if indegree[nn] == 0:
                q.append(nn)
    return "\n".join(res) if len(res) == nodes else "IMPOSSIBLE"

print(kahn(n, g, indegree))

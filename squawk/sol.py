from collections import defaultdict, deque

n, m, s, t = map(int, input().split(" "))

g = defaultdict(list)

for _ in range(m):
    n1, n2 = map(int, input().split(" "))
    g[n1].append(n2)
    g[n2].append(n1)

q = deque([s])

for l in range(t):
    for _ in range(len(q)):
        n = q.popleft()
        for nn in g[n]:
            q.append(nn)
print(len(q))

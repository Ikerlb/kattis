from math import inf
from collections import deque, defaultdict

n, h, l = map(int, input().split(" "))

q = deque(map(int, input().split(" ")))
g = defaultdict(list)

for _ in range(l):
    a, b = map(int, input().split(" "))
    g[a].append(b)
    g[b].append(a)

dists = [inf for _ in range(n)]
for h in q:
    dists[h] = 0

d = 0
while q:
    for _ in range(len(q)):
        n = q.popleft()    
        for nn in g[n]:
            if dists[nn] == inf:
                dists[nn] = d + 1        
                q.append(nn)
    d += 1

#print(max(enumerate(dists), key = lambda x: (x[1], x[0]))[0])
print(max(enumerate(dists), key = lambda x: (x[1], -x[0]))[0])
#print(list(enumerate(dists)))

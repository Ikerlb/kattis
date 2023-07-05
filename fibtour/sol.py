from collections import defaultdict
from itertools import chain

fibos = [1, 1]

while fibos[-1] <= 10 ** 18:
    fibos.append(fibos[-2] + fibos[-1])

dfibos = {f:i for i, f in enumerate(fibos)}

n, m = map(int, input().split(" "))

heights = [int(s) for s in input().split(" ")]

g = defaultdict(list)

one_one = set()

for _ in range(m):
    s, t = map(lambda x: int(x) - 1, input().split(" "))
    hs = heights[s]
    ht = heights[t]

    if ht < hs:
        s, t = t, s
        hs, ht = ht, hs

    if not hs in dfibos: 
        continue
    if not ht in dfibos:
        continue
    if ht == hs == 1: 
        one_one.add(t)
        one_one.add(s)
    elif dfibos[ht] - dfibos[hs] == 1:
        g[s].append(t)

def toposort(g, n, used, indices):
    used.add(n)
    for nn in g[n]:
        if nn not in used:
            toposort(g, nn, used, indices)
    indices.append(n) 

indices = []
used = set()
for i in range(n):
    if i not in used:
        toposort(g, i, used, indices)
indices.reverse()

dist = defaultdict(int)
for i in range(n):
    if heights[i] == 1 and i in one_one:
        dist[i] = 2
    elif heights[i] in dfibos:
        dist[i] = 1

res = 0 
for i in indices:
    res = max(res, dist[i])
    for nn in g[i]:
        dist[nn] = max(dist[nn], dist[i] + 1)

print(res)

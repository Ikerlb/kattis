from collections import defaultdict
from heapq import heappush, heappop
from math import inf

def djikstra(g, s, dists):
    dists[s] = 0
    h = []
    heappush(h, (0, s))
    while h:
        d, u = heappop(h)
        if d > dists[u]:
            continue
        for v, w in g[u]:  
            if w + dists[u] < dists[v]: # relax edge
                dists[v] = dists[u] + w
                heappush(h, (dists[v], v))

tc = 0
while True:
    n, m, q, s = map(int, input().split(" "))
    if n == m == q == s: 
        break
    if tc > 0:
        print()
    dists = [inf for _ in range(n)]
    g = defaultdict(list)
    for _ in range(m): 
        u, v, w = map(int, input().split(" "))
        g[u].append((v, w))
    djikstra(g, s, dists)
    for _ in range(q):
        qq = int(input())
        if dists[qq] != inf:
            print(dists[qq])
        else:
            print("Impossible")
    tc += 1

from collections import deque, defaultdict
from heapq import heappush, heappop
from math import inf

tc = int(input())
input() ## burn first blank line

def djikstra(g, h, dists):
    for _, n in h:
        dists[n] = 0
    while h:
        w, n = heappop(h)
        for nn, ww in g[n]:
            if w + ww < dists[nn]:
                heappush(h, (w + ww, nn))
                dists[nn] = w + ww

for _ in range(tc):
    f, i = map(int, input().split(" "))
    fs, g = [], defaultdict(list)
    for _ in range(f):
        fs.append(int(input()) - 1)    
    while True:
        try:
            line = input()
        except:
            break
        if not line:
            break    
        s, e, w = map(int, line.split(" "))
        s, e = s - 1, e - 1
        g[s].append((e, w))
        g[e].append((s, w))

    h = []
    dists = [inf] * i
    for n in fs:
        heappush(h, (0, n))
    djikstra(g, h, dists)
    og_dists = dists[:]
    m_dist, m_idx  = max(dists), 0
    for n in range(i):
        dists[:] = og_dists[:]
        heappush(h, (0, n))
        djikstra(g, h, dists)
        cm = max(dists)
        if cm < m_dist:
            m_dist, m_idx = cm, n
    print(m_idx + 1)

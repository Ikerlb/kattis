from collections import defaultdict, deque

n = int(input())

g = defaultdict(set)

for _ in range(n):
    l = input().split(" ")
    g[l[0]] = set(l[1:])
    for nn in g[l[0]]:
        g[nn].add(l[0])    

def bfs(g, start, end):
    q = deque([start])
    v = {start:None}
    while q:
        n = q.popleft()
        if n == end:
            return v    
        for nn in g[n]:
            if nn not in v:
                v[nn] = n
                q.append(nn)
    return None

src, tgt = input().split(" ")
visited = defaultdict(int)

idfk = bfs(g, src, tgt)
if idfk is None:    
    print("no route found")
else:
    n = tgt
    res = []
    while n is not None:
        res.append(n)
        n = idfk[n]
    print(" ".join(reversed(res)))
    

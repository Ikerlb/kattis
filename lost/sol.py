from collections import defaultdict, deque
from math import inf

n, m = map(int, input().split(" "))
langs = {v:i for i, v in enumerate(input().split(" "), 1)}
langs["English"] = 0
target = set(langs.keys())

g = defaultdict(list)
edges = [[0 for _ in range(len(langs))] for _ in range(len(langs))]

for _ in range(m):
    n1, n2, w = input().split(" ")
    w = int(w)
    g[n1].append((n2, w))
    g[n2].append((n1, w))
    i = langs[n1]
    j = langs[n2]
    edges[i][j] = w
    edges[j][i] = w
    


q = deque([("English", 0, None)])
dists = defaultdict(lambda: (inf, inf, None))
dists["English"] = (0, 0, None)
steps = 0

while q:
    for _ in range(len(q)):
        n, w, p = q.popleft()
        if dists[n][0] < steps:
            continue
        elif dists[n][1] > w:
            dists[n] = (steps, w, p)
        for nn, ww in g[n]:
            if dists[nn][0] == inf:
                q.append((nn, w + ww, n))
    steps += 1

res = 0
for k in dists:
    _, w, p = dists[k]
    if w != inf:
        target.discard(k)
    if p is not None:
        target.discard(p)
        i = langs[k]
        j = langs[p]
        res += edges[i][j]

if not target:
    print(res)
else:
    print("Impossible")

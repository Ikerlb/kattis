from collections import defaultdict, deque
import sys

# i mean i'm kinda tired and
# didn't want to think how to
# do this with my own stack
sys.setrecursionlimit(100000)

n = int(input())
g = defaultdict(list)

for _ in range(n):
    l = input()
    if l[-1] != ":":       
        n, nns = l.split(":")
        for nn in nns.split(" "):
            g[nn].append(n)

def dfs(g, v, n, l):
    for nn in g[n]:    
        if nn not in v:
            v.add(nn)
            dfs(g, v, nn, l)
    l.append(n)

n = input()
v = set()
v.add(n)
l = []
dfs(g, v, n, l)
print("\n".join(reversed(l)))

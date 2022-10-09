from collections import defaultdict, deque
from functools import lru_cache

n, m, k = map(int, input().split(" "))

colors = list(map(lambda x: int(x) - 1, input().split(" ")))

g = defaultdict(list)

for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split(" "))
    g[a].append(b)
    g[b].append(a)

@lru_cache(None)
def dp(i, mask):
    res = 0
    nmask = mask | (1 << colors[i])
    for nn in g[i]:
        if nmask & (1 << colors[nn]) == 0:
            res += dp(nn, nmask) + 1
    #print(i, bin(mask), res)
    return res

#print(g)
print(sum(dp(i, 0) for i in range(n)))
#for i in range(n):
#    print(f"{i} -> {dp(i, 0)}")

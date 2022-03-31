from itertools import permutations
from math import inf

n = int(input())
routines = [input() for _ in range(n)]


m = inf
for p in permutations(routines):
    res = 0
    for i in range(len(p) - 1):
        res += sum(1 for c in p[i] if c in p[i + 1])            
    m = min(m, res)
print(m)


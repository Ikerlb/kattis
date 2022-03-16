from bisect import bisect_left
from collections import defaultdict

def hits(stalag, stalac, b2th, t2bh):
    i1 = bisect_left(stalag, b2th)
    i2 = bisect_left(stalac, t2bh)
    return len(stalag) - i1 + len(stalac) - i2

n, h = map(int, input().split(" "))
stalagmites = []
stalactites = []

for i in range(n):
    nn = int(input())
    if i % 2 == 0:
        stalagmites.append(nn)
    else:
        stalactites.append(nn)

stalagmites.sort()
stalactites.sort()

c = defaultdict(int)
for j in range(1, h + 1):
    c[hits(stalagmites, stalactites, j, h - j + 1)] += 1
m = min(c)
print(f"{m} {c[m]}")

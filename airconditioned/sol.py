from math import inf

n = int(input())

events = []
for _ in range(n):
    events.append(tuple(map(int, input().split(" "))))

events.sort()

cs, ce = -inf, inf
res = 1
for s, e in events:
    if cs <= s <= ce or cs <= e <= ce:
        cs = min(cs, s)
        ce = min(ce, e)
    else: 
        cs, ce = s, e
        res += 1
print(res)

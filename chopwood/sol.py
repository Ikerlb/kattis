from heapq import heapify, heappush, heappop
from collections import Counter

n = int(input())

l = [int(input()) for _ in range(n)]

def verify(l):
    c = Counter() 
    for src, tar in l:
        c[src] += 1
        c[tar] += 1

    h = [n for n in c if c[n] == 1]
    heapify(h)

    for src, tar in l:
        n = heappop(h)    
        if n != src:
            return False
        if c[src] != 1:
            return False
        c[tar] -= 1
        if c[tar] == 1:
            heappush(h, tar)    

    return True
        

def build(l):
    n = len(l) + 1
    c = Counter()
    for i in range(1, n + 1):
        c[i] = 0
    for node in l: 
        c[node] += 1

    h = [n for n in c if c[n] == 0]
    heapify(h)

    res = []
    for node in l:
        res.append((heappop(h), node))
        c[node] -= 1
        if c[node] == 0:
            heappush(h, node)
    return res

res = build(l)
if verify(res):
    print("\n".join(str(n) for n, _ in res))
else:
    print("Error")

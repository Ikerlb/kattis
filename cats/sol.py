from collections import defaultdict, deque
from heapq import heappush, heappop

class DSU:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def _root(self, a):
        if self.parents[a] == a:
            return a
        ra = self._root(self.parents[a])
        self.parents[a] = ra
        return self.parents[a]

    def find(self, a):
        return self._root(a)

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return False

        self.parents[ra] = rb
        return True

tcs = int(input())
for _ in range(tcs):
    M, C = map(int, input().split(" "))
    g = defaultdict(list)
    s, total = [], 0

    dsu = DSU(C)
    for _ in range((C * (C - 1)) // 2):
        c1, c2, d = map(int, input().split(" "))
        s.append((d, c1, c2))

    s.sort(reverse = True)
    while s:
        d, c1, c2 = s.pop()
        if not dsu.union(c1, c2):        
            continue
        total += d    
        C -= 1 
        if C == 0: # finish early
            break
    print("yes" if M >= total else "no")

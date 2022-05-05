from collections import defaultdict

class Dsu:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    #def _root(self, a):
    #    if self.parents[a] == a:
    #        return a
    #    ra = self._root(self.parents[a])
    #    self.parents[a] = ra
    #    return ra
    def _root(self, a):
        root = a 
        while self.parents[root] != root:
            root = self.parents[root]
        while a != root: 
            a, self.parents[a] = self.parents[a], root
        return root
            

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return False

        self.parents[ra] = rb
        return True

    def find(self, a):
        return self._root(a)

#g = defaultdict(list)

n = int(input())
s = []
dsu = Dsu(n)
for r in range(n):
    row = [int(w) for w in input().split()]
    for c in range(r + 1, n):
        s.append((row[c], r, c))    

s.sort()

res = []
for i in range(len(s)):
    _, n1, n2 = s[i]
    if not dsu.union(n1, n2):
        continue    
    res.append((n1, n2))
for n1, n2 in res:
    print(n1 + 1, n2 + 1)

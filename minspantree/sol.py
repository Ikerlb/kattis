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

while True:
    n, m = map(int, input().split(" "))
    if n == m == 0:
        break
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split(" "))
        edges.append((w, u, v))

    edges.sort()  
    dsu = Dsu(n)
    tree, dist = [], 0
    for w, u, v in edges:
        #print(tree, dist)
        if not dsu.union(u, v):    
            continue
        dist += w
        tree.append(sorted((u, v)))
        n -= 1
        if n == 1:
            print(dist)
            print("\n".join(f"{u} {v}" for u, v in sorted(tree))) 
            break
    else:
        print("Impossible")


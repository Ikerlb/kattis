from sys import stdin

class UFS:
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def _root(self, a):
        if self.parents[a] == a:
            return a
        self.parents[a] = self._root(self.parents[a])
        return self.parents[a]

    def union(self, a, b):
        ra = self._root(a)    
        rb = self._root(b)

        if ra == rb:
            return True

        self.parents[ra] = rb
        self.sizes[rb] += self.sizes[ra]
        return False

    def size(self, a):
        ra = self._root(a)
        return self.sizes[ra]

    def decrement(self, a):
        ra = self._root(a)
        self.sizes[ra] = max(self.sizes[ra] - 1, 0)

    def __repr__(self):
        return f"parents {self.parents}\nsize {self.sizes}"


items, n = map(int, input().split(" "))
ufs = UFS(n)
#print(ufs)

for _ in range(items):
    a, b = map(lambda x: int(x) - 1, input().split(" "))
    if ufs.size(a) + ufs.size(b) > 0:
        ufs.union(a, b)
        ufs.decrement(a)
        print("LADICA")
    else:
        print("SMECE")

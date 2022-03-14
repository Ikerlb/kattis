class Fenwick:
    def __init__(self, n):
        self.arr = [0] * (n + 1)
        
    def add(self, i, delta):
        i += 1
        while i < len(self.arr):
            self.arr[i] += delta
            i += i & (-i)

    def _query(self, i):
        res = 0 
        while i > 0:
            res += self.arr[i]
            i -= i & (-i)
        return res

    def query(self, l, r):
        return self._query(r + 1) - self._query(l)

n, q = map(int, input().split(" "))
trees = [Fenwick(n) for _ in range(6)]        
values = [int(c) for c in input().split(" ")]
types = [0] * n

for i, c in enumerate(input()):
    types[i] = int(c) - 1
    trees[int(c) - 1].add(i, 1) 

for _ in range(q):
    op, fst, snd = map(int, input().split(" "))
    if op == 1:
        fst -= 1
        snd -= 1

        trees[types[fst]].add(fst, -1)
        types[fst] = snd
        trees[snd].add(fst, 1)
    elif op == 2:
        fst -= 1
        values[fst] = snd
    else:
        fst -= 1
        snd -= 1
        res = 0
        for g in range(len(values)):
            res += trees[g].query(fst, snd) * values[g]
        print(res)
        

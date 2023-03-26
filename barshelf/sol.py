from bisect import bisect_left

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, idx, val):
        idx += 1
        while idx <= self.n:
            self.bit[idx] += val
            idx += idx & -idx

    def _query(self, idx):
        res = 0
        while idx > 0:
            res += self.bit[idx]
            idx -= idx & -idx
        return res

    def query(self, l, r):
        return self._query(r + 1) - self._query(l)

    def __repr__(self):
        return ",".join(str(self.query(0, i)) for i in range(self.n))

_ = int(input())
A = list(map(int, input().split()))

S = sorted(set(A))
D = {a:i for i, a in enumerate(S)}

rite = BIT(len(D))
left = BIT(len(D))

for n in A:
    rite.update(D[n], 1)

res = 0
for i, n in enumerate(A):
    rite.update(D[n], -1)
    
    ri = bisect_left(S, n >> 1)
    if S[ri] != n >> 1:
        ri -= 1
    li = bisect_left(S, n << 1)

    r = rite.query(0, ri)
    l = left.query(li, len(S) - 1)

    res += r * l
    left.update(D[n], 1)

print(res)

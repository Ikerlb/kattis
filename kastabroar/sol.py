class UFS:
    def __init__(self, n):
        self.parents = [i for i in range(n)]

    def _root(self, a):
        if self.parents[a] == a:
            return a
        ra = self._root(self.parents[a])
        self.parents[a] = ra
        return ra

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)

        if ra == rb:
            return False

        self.parents[ra] = rb
        return True

    def groups(self):
        s = set()
        for i in range(len(self.parents)):
            s.add(self._root(i))
        return list(s)

def solve(n, edges):
    ufs = UFS(n)
    spare = []

    for a, b in edges:
        if not ufs.union(a, b):
            spare.append((a, b))

    res = ["Ja"]
    g = ufs.groups()
    res.append(f"{len(g) - 1}")
    for sp, i in zip(spare, range(1, len(g))):
        sa, sb = sp
        na, nb = g[i - 1], g[i]
        res.append(f"{sa + 1} {sb + 1} {na + 1} {nb + 1}")
    return "\n".join(res)

def parse(pair):
    a, b = map(lambda x: int(x) - 1, pair.split(" "))
    return a, b

n, m = map(int, input().split(" "))
if m < (n - 1):
    print("Nej")
else:
    edges = [parse(input()) for _ in range(m)]
    print(solve(n, edges))

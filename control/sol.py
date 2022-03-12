class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]

    def _root(self, a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self._root(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        ra = self._root(a)
        rb = self._root(b)
        if ra == rb:
            return False
        self.parent[ra] = rb
        self.size[rb] += self.size[ra]
        return True

    def find(self, a):
        return self._root(a)

    def same(self, a, b):
        return self._root(a) == self._root(b)

def concoct(ingredients, ufs):
    group = set()
    res = 0
    for ing in ingredients:
        g = ufs.find(ing)
        if g not in group:
            group.add(g)
            res += ufs.size[g]

    if len(ingredients) == res:
        fst = group.pop()
        for g in group: 
            ufs.union(fst, g)
        return True
    return False

n = int(input())

recipes = []
m = 0
for _ in range(n):
    line = input()
    ingredients = [int(s) for s in line.split(" ")[1:]]
    m = max(m, *ingredients)
    recipes.append(ingredients)  

ufs = UnionFind(m + 1)
print(sum(1 for ingredients in recipes if concoct(ingredients, ufs)))

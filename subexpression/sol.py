class Node:
    def __init__(self, f, left = None, right = None):
        self.f = f
        self.left = Node(left) if type(left) is str else left
        self.right = Node(right) if type(right) is str else right 
        if right is None and left is None:
            self.h = hash(f)
        else:
            self.h = hash((hash(f), hash(left), hash(right)))

    def __hash__(self):
        return self.h

    def __repr__(self):
        if self.left is None and self.right is None:
            return self.f
        return f"{self.f}({self.left},{self.right})"

def tokenize(s):
    cur, res = [], []
    for c in s:
        if c in "()," and cur:
            res.append("".join(cur))
            cur.clear()
            res.append(c)
        elif c in "(),":
            res.append(c)
        else:
            cur.append(c)
    if cur:
        res.append("".join(cur))
    return res

def parse(tokens):
    s = [[]]
    for t in tokens:
        if t == "(":
            s.append([])
        elif t == ")":
            s1, s2 = s.pop()
            t = s[-1].pop()
            e = Node(t, s1, s2)
            s[-1].append(e)
        elif t == ",":
            continue
        else:
            s[-1].append(t)
    return s.pop().pop()

# iter dfs
def dfs(node):
    s = [node]
    res = [[]]
    
    d = {}
    i = 1

    while s:
        n = s.pop()
        if hash(n) in d:
            res[-1].append(d[hash(n)])
        else:
            d[hash(n)] = i

            i += 1

            if n.right is not None and n.left is not None:
                res.append([])
                s.append(n.right)
                s.append(n.left)
            res[-1].append(n.f)
        while res and len(res[-1]) == 3:
            t, s1, s2 = res.pop()
            res[-1].append(f"{t}({s1},{s2})")
    return res.pop().pop()

n = int(input())

for _ in range(n):
    s = input()
    tokens = tokenize(s)
    if len(tokens) == 1:
        print(s)
        continue
    node = parse(tokens)
    print(dfs(node))

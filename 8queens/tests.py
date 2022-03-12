from random import randint

def dfs(r, cols, ldiags, rdiags, res):
    if r == -1:
        res.append(cols[:]) 
        return
    for c in range(len(cols)):
        rd = r + c
        ld = len(cols) + r - c 
        if cols[c] is not None or (ld in ldiags) or (rd in rdiags):
            continue        
        cols[c] = r
        ldiags.add(ld)
        rdiags.add(rd)
        dfs(r - 1, cols, ldiags, rdiags, res)
        cols[c] = None
        ldiags.remove(ld)
        rdiags.remove(rd)

def decode(cols):
    s = []
    for r in range(len(cols)):
        row = []
        for c in range(len(cols)):
            row.append("*" if cols[c] == r else ".")
        s.append("".join(row))
    return "\n".join(s)

res = []
n = 8
cols = dfs(n - 1, [None] * n, set(), set(), res)
for p in res:
    print(decode(p), end = "\n\n")

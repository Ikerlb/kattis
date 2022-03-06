from itertools import product, repeat

def expression(prod, val):
    res = []
    for o, v in zip(prod, repeat(val)):
        res.append(str(v))
        res.append(o)    
    return res + [str(val)]

m = {}
for p in product(["+","*","//","-"], repeat = 3):
    e = expression(p, 4)
    res = int(eval("".join(e)))
    m[res] = f"{' '.join(e)} = {res}"

k = int(input())

for _ in range(k):
    n = int(input())
    if n in m:
        print(m[n].replace("//", "/"))
    else:
        print("no solution")

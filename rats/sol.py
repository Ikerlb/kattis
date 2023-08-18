import re

def reverse(n):
    res = 0
    while n > 0:
        n, d = divmod(n, 10)
        res = (res * 10) + d
    return res

def digits(n):
    l = []
    while n > 0:
        n, d = divmod(n, 10)
        l.append(d)
    return l

def _next(n):
    s = n + reverse(n)
    l = sorted(digits(s), reverse = True)
    while l and l[-1] == 0:
        l.pop()
    return sum(pow(10, i) * d for i, d in enumerate(l))

def is_creeper(val):
    val = str(val)
    if (val.startswith("1233") and val.endswith("34444")):
        rep = val[3:-4]
        return rep == len(rep) * rep[0]
    if (val.startswith("5566") and val.endswith("67777")):
        rep = val[3:-4]
        return rep == len(rep) * rep[0]
    return False

def solve(m, val):
    s = set()
    prev = None
    for i in range(1, m + 1):
        if is_creeper(val):
            return f"C {i}"
        elif val in s:
            return f"R {i}"
        s.add(val)
        prev = val
        val = _next(val)
    return str(prev)

tcs = int(input())

for _ in range(tcs):
    k, m, val = map(int, input().split(" "))
    res = solve(m, val)
    print(f"{k} {res}")

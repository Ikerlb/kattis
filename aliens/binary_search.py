from sys import stdin
from collections import Counter
from random import randint

def f(c):
    return ord(c) - ord('a') + 1

def _hash(s, b, p):
    h = 0
    for i, c in enumerate(reversed(s)):
        h = (h + (f(c) * pow(b, i, p)) % p) % p
    return h

def hashes_brute(s, k, b, p):
    for i in range(0, len(s) - k + 1):
        yield _hash(s[i:i + k], b, p)

def hashes(s, k, b, p):
    h = _hash(s[:k], b, p)    
    yield h
    for i in range(k, len(s)):
        h = (h - (f(s[i - k]) * pow(b, k - 1, p)) % p) % p
        h = (h * b) % p
        h = (h + f(s[i])) % p
        yield h

def test(s, b, p):
    for k in range(1, len(s)):
        for h1, h2 in zip(hashes(s, k, b, p), hashes_brute(s, k, b, p)):
            print(h1, h2, k)
            assert(h1 == h2)

# if there is a substring of size k
# that repeats more than or exactly k
# times there is obviously a substring
# of size < k that repeats more than
# or exactly k
def _try(s, k, m, b, p):
    d = {}
    for i, h in enumerate(hashes(s, k, b, p)):
        if h not in d:
            d[h] = [1, i]
        else:
            d[h][0] += 1
            d[h][1] = i

    l = list(d.values())
    l.sort(key = lambda x: (x[1], x[0]), reverse = True)

    for freq, last in l:
        if freq >= m:
            return last
    return None

# we want last to be true
def solve(s, m, b, p):
    l, r = 1, len(s)
    res = None
    while l <= r:
        mid = (l + r) >> 1
        if (t := _try(s, mid, m, b, p)) is None:
            r = mid - 1
        else:
            res = (mid, t)
            l = mid + 1
    if res is None:
        return "none"
    return f"{res[0]} {res[1]}"

while (m := int(next(stdin))) != 0:
    s = next(stdin)
    b = 31
    #p = 10 ** 9 + 7
    p = 18361375334787046697
    print(solve(s[:-1], m, b, p))


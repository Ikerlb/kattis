from math import isqrt
from collections import Counter

def divisors(n):
    for i in range(1, n):
        d, m = divmod(n, i)
        if m == 0:
            yield i, d

def counter_chunks(s, n):
    for i in range(0, len(s), n):
        yield Counter(s[i:i+n])

def works(s, i):
    w = Counter(s[:i])
    #print(f"{s=} {w=} {i=}")
    return all(w == cc for cc in counter_chunks(s, i))


s = input()
for d1, d2 in divisors(len(s)):
    if works(s, d1):
        print(s[:d1])
        break
else:
    print(-1)

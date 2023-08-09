from math import isqrt

def chunks(s, k):
    for i in range(0, len(s), k):
        yield s[i:i + k]

# returns whether
# or not s1 is
# s2 rotated once
# to the right
def is_one_rotated(s1, s2):
    n = len(s1)
    for i in range(n):
        if s1[i] != s2[(i + 1) % n]:
            return False
    return True

def is_k_cyclic(s, k):
    prev = None
    for c in chunks(s, k):
        if prev is not None and not is_one_rotated(prev, c):
            return False
        prev = c
    return True

def multiples(n):
    s = set()
    for i in range(1, isqrt(n) + 1):
        d, m = divmod(n, i)
        if m == 0:
            s.add(d)
            s.add(i)
    return sorted(s)


s = input()

for m in multiples(len(s)):
    if is_k_cyclic(s, m):
        print(m)
        break

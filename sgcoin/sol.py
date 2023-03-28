from itertools import product

def ok(h):
    return h % (10 ** 7) == 0

def poss(max_num, trailing):
    smn = str(max_num)
    head, rest = smn[:-trailing], smn[-trailing:]
    for i in range(int(head)):
        yield i * 10 ** trailing

def step(s, prev):
    v = prev
    for c in s:
        v = (v * 31 + (ord(c))) % 1000000007
    return (v * 7) % 1000000007 

def H(prev, s, token):
    v = step(s, prev)
    return (v + token) % 1000000007


possible_hashes = list(poss(1000000007, 7))

def solve(s1, s2, prev):
    s = step(s1, prev)
    p1l = list((h - s) % 1000000007 for h in possible_hashes if h >= s)
    p1 = p1l.pop()
    s = step(s2, H(prev, s1, p1))
    p2l = list((h - s) % 1000000007 for h in possible_hashes if h >= s)
    p2 = p2l.pop()
    #print(f"{p1l=}, {p2l=}")
    print(s1, p1)
    print(s2, p2)


previous_hash = 140000000
s1 = "charlie-pays-to-eve-9-sg-coins"
s2 = "icpc-sg-2018-at-nus"
solve(s1, s2, previous_hash)

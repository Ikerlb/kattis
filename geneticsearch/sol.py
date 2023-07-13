from collections import Counter

def _hash(s, d, q):
    return sum((d[c] * ((len(d)+1) ** i)) % q for i, c in enumerate(reversed(s))) % q

def rabin_karp_hashes(s, ws, q, d):
    base = len(d) + 1

    c = Counter()
    
    sh = _hash(s[:ws], d, q)
    c[sh] += 1

    for i in range(ws, len(s)):
        li = i - ws

        sh -= d[s[li]] * (base ** (ws - 1))
        sh *= base
        sh += d[s[i]]
        sh = sh % q

        c[sh] += 1

    return c

def remove_one(s):
    res = set()
    for i in range(len(s)):
        res.add(s[:i] + s[i + 1:])
    return res

def add_one(s, d):
    res = set()
    for i in range(len(s) + 1):
        for c in d.keys(): 
            res.add(s[:i] + c + s[i:])
    return res

d = {
    "A": 1,
    "G": 2,
    "C": 3,
    "T": 4,
}

q = 10 ** 9 + 7

while True:
    l = input()
    if l == "0":
        break

    p, s = l.split(" ")
    c = rabin_karp_hashes(s, len(p), q, d)
    cmo = rabin_karp_hashes(s, len(p) - 1, q, d)
    cpo = rabin_karp_hashes(s, len(p) + 1, q, d)

    t1 = c[_hash(p, d, q)]
    t2 = sum(cmo[_hash(pmo, d, q)] for pmo in remove_one(p))
    t3 = sum(cpo[_hash(ppo, d, q)] for ppo in add_one(p, d))

    print(f"{t1} {t2} {t3}")

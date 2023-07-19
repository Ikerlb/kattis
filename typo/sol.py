def f(a):
    return (ord(a) - ord('a')) + 1

def _hash(s, p):
    return sum((f(a) * pow(26, i)) % p for i, a in enumerate(reversed(s)))

def hashes(s, p):
    hl = 0
    hr = _hash(s, p)
    n = len(s) - 1
    for i,c in enumerate(s):

        comp = (f(c) * pow(26, n - i))
        compm1 = (f(c) * pow(26, n - i - 1))
        hr -= (comp % p)
        hmo = (hl + hr) % p
        yield hmo
        hl += (compm1 % p)

n = int(input())
words = [input() for _ in range(n)]

p = 10 ** 9 + 7
s = {_hash(word, p) for word in words}

res = []
for word in words:
    if any(hs in s for hs in hashes(word, p)):
        res.append(word)

if not res:
    print("NO TYPOS")
else:
    print("\n".join(res))

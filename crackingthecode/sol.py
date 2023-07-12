from string import ascii_lowercase

def bijection(encr, plain):
    if (len(encr) != len(plain)):
        return None
    sub = {}
    vals = set()
    for c, p in zip(encr, plain):
        if c in sub and sub[c] != p:
            return None
        elif c in sub:
            continue
        elif p in vals:
            return None
        else:
            sub[c] = p
            vals.add(p)
    return sub if sub else None

def encrypt(text, key):
    res = []
    for c in text:
        if c in key:
            res.append(key[c])
        else:
            res.append("?")
    return "".join(res)

def merge(s1, s2):
    res = {}
    for k, v in s1.items():
        if k in s2 and v == s2[k]: 
            res[k] = v
    return res

def solve(encrypted, plain, message):
    key = None
    for encr in encrypted:
        if (res:=bijection(encr, plain)) is not None and key is not None:
            key = merge(key, res)
        elif res is not None:
            key = res

    if key is None:
        return "IMPOSSIBLE"

    # if you can safely substitute 25 chars, you obviously can do 26
    if key and len(key) == 25:
        unc = set(ascii_lowercase) - set(key.keys())
        unp = set(ascii_lowercase) - set(key.values())
        key[unc.pop()] = unp.pop()

    return encrypt(message, key)

tcs = int(input())

for _ in range(tcs):
    ms = int(input())
    encrypted = [input() for _ in range(ms)]
    plain = input()
    message = input()

    print(solve(encrypted, plain, message))

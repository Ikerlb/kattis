mode = input()
n = int(input())

VOWELS = 'aeiouy'

def encrypt(s):
    res = []    
    for c in text:
        if c in VOWELS:
            res.append(f"ub{c}")
        elif c in VOWELS.upper():
            res.append(f"Ub{c}")
        else:
            res.append(c)
    return "".join(res)

def decrypt(s):
    i = 0
    res = []
    while i < len(s):
        if s[i:i + 2].lower() == "ub" and s[i + 2] in VOWELS:
            res.append(s[i + 2] if s[i].islower() else s[i + 2].upper())
            i += 3
        else:
            res.append(s[i])
            i += 1
    return "".join(res)

for _ in range(n):
    text = input()
    if mode == "D":
        print(encrypt(text))
    else:
        print(decrypt(text))
print()

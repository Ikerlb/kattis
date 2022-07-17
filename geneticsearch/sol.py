def z_array(p):
    prefix = [0 for _ in range(len(p))]
    j = None
    while i < len(p):
        while j is not None and p[i] != p[j]:
            j = p[j]
        j += 1
        i += 1
        p[i] = j
    return prefix

def kmp(p, s, z):
    i = j = 0
    res = 0
    while i < len(p):
        while j >= 0 and p[j] != s[i]:
            j = z[j]
        i += 1
        j += 1
        if j == len(p):
            res += 1
    return res

while True:
    l = input()
    if l == "0":
        break
    p, s = input().split(" ")
    z = z_array(p)
    print(kmp(p, s, z))
    



width = 0.42044820762685725
height = 0.5946035575013605

def tape_needed(l):
    need = 2
    for i, have in enumerate(l):    
        need = need - have 
        if need <= 0:
            return i, have + need
        need *= 2
    return None

def solve(l):
    res = tape_needed(l)
    if res is None:
        return "impossible"
    s = 0
    i, need = res
    l[i] = need

    for j in range(i, -1, -1):
        dj, mj = divmod(j, 2)
        ljh = l[j] // 2
        if mj == 1:
            s += ((width / (2 ** dj)) * ljh)
        else:
            s += ((height / (2 ** dj)) * ljh)
        l[j - 1] += ljh
    return s

n = int(input())
l = [int(n) for i, n in enumerate(input().split(" "))]
print(solve(l))

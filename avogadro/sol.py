from collections import deque, Counter

# or to read a different way
# if we are missing one item
# from either the second or the third
# we NEED to remove that column on the first
# (and its same indices in snd and thd)
# we basically do that until we are done

def solve(a1, a2, a3):
    i2a = {n:i for i, n in enumerate(a1)}
    c = Counter(a1)
    c2 = Counter(a2)
    c3 = Counter(a3)

    res = []
    q = deque()
    for i in range(1, len(a1) + 1):
        #print(i, q)
        if c[i] and c2[i] == 0:
            q.append(i)
            res.append(i)
            c[i] -= 1
        if c[i] and c3[i] == 0:
            res.append(i)
            q.append(i)
            c[i] -= 1

    while q:
        n = q.popleft()
        i = i2a[n]
        v2 = a2[i]
        c2[v2] -= 1
        if c2[v2] == 0 and c[v2] == 1:  
            q.append(v2)
            res.append(v2)
            c[v2] -= 1

        v3 = a3[i]
        c3[v3] -= 1
        if c3[v3] == 0 and c[v3] == 1:
            q.append(v3)
            res.append(v3)
            c[v3] -= 1
    return res

_ = input()
a1 = [int(n) for n in input().split()]
a2 = [int(n) for n in input().split()]
a3 = [int(n) for n in input().split()]

res = solve(a1, a2, a3)
#print(res)
print(len(res))

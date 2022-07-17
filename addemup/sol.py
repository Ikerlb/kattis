from collections import defaultdict

m = {
    0: 0,
    1: 1,
    2: 2,
    5: 5, 
    6: 9,
    8: 8,
    9: 6,
}

def reversible(n):
    res = 0
    while n:    
        n, d = divmod(n, 10)    
        if d in [3, 4, 7]:
            return None
        res = (res * 10) + m[d]
    return res

def can_solve(s, d):
    for n in d:
        if (s - n) == n and len(d[n]) > 1:
            return True
        elif (s - n) in d and len(d[s - n]) == 1 and d[s - n] == d[n]:
            continue
        elif (s - n) in d:
            return True    
    return False

n, s = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))
d = defaultdict(set)

for i, n in enumerate(nums):
    #st.add(n)
    d[n].add(i)
    r = reversible(n)
    if r is not None:
        d[r].add(i)

print("YES" if can_solve(s, d) else "NO")

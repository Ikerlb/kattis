from random import randint

def solve(n):
    for i in range(0, n + 1):
        for j in range(i):
            if (i * i) - (j * j) == n:        
                return j, i
    return None

d = int(input())
res = solve(d)
if res is None:
    print("impossible")
else:
    n, m = res
    print(f"{n} {m}")

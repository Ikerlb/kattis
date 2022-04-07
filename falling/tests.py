from random import randint

def solve(n):
    for i in range(1, n):
        for j in range(i):
            if (i * i) - (j * j) == n:        
                return j, i
    return None

n = randint(1, 200_000)

with open("/tmp/falling.in", "w") as f:
    f.write(str(n))
    
with open("/tmp/falling.ans", "w") as f:
    res = solve(n)    
    f.write(f"{res[0]} {res[1]}\n" if res is not None else "impossible")



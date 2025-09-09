from sys import stdin
from math import isqrt
from collections import Counter
import fileinput

def pth_order(n, p):
    i = 0
    while n % p == 0:
        i += 1
        n //= p 
    return i

def solve(n): 
    if n < 10:
        return [1, n]
    res = [] 
    for i in reversed(range(2, 10)):
        d = pth_order(n, i)
        #print(f"{n=}, {i=}, {d=}")
        if d > 0:
            res.extend([i] * d)
            n //= (i ** d)
    if n != 1:
        return None
    return sorted(res)

for line in fileinput.input():
    n = int(line[:-1])
    if n == -1:
        break 
    res = solve(n) 
    if res is None:
        print("There is no such number.")
    else:
        print("".join(map(str, res)))


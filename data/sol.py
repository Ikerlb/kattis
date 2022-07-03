import math
from functools import lru_cache

def primes(upto):
    p = [0 for _ in range(upto + 1)]
    for i in range(2, upto + 1):
        if p[i] == 0:
            for j in range(2 * i, upto + 1, i):
                p[j] += 1
    return p

def idfk(n):
    i = 0
    res = 0
    while n:
        if n & 1 == 1:
            res += nums[i]
        n >>= 1
        i += 1
    return res

@lru_cache(None)
def dp(mask):
    if mask == 0:
        return 0
    s = mask
    mx = -math.inf
    while s > 0:           
        s = (s - 1) & mask
        xor = s ^ mask
        mx = max(mx, p[idfk(xor)] + dp(s))
    return mx

p = primes(14000)
for i in range(2, len(p)):
    if p[i] == 0:
        p[i] = 1

#nums = [4, 7, 8]
#nums = [2,3,4,5,8]
#m = (1 << len(nums)) - 1

n = int(input())
nums = list(map(int, input().split(" ")))
m = (1 << len(nums)) - 1
print(dp(m))

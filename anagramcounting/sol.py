from collections import Counter, defaultdict
from sys import stdin


def factors(n):
    i = 2    
    while n > 1:
        pw = 0
        while n % i == 0:     
            n //= i    
            pw += 1
        if pw > 0:    
            yield i, pw    
        i += 1

# ugh
def anagrams(s):
    if not s:
        return 0
    mpf = defaultdict(int)
    for i in range(1, len(s) + 1):
        for k, v in factors(i):
            mpf[k] += v
    for _, v in Counter(s).items():
        for i in range(1, v + 1):
            for kk, vv in factors(i):
                mpf[kk] -= vv    
    res = 1
    for k, v in mpf.items():
        res *= (k ** v)
    return res
    

for line in stdin:
    line = line[:-1]
    print(anagrams(line))

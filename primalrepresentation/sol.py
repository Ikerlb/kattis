from sys import stdin
from math import ceil

def sieve(upto):
    primes = []    
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:    
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

def prime_factors(n):
    i = 0
    res = []
    while n != 1 and i < len(primes):
        times = 0
        while (n % primes[i]) == 0:
            n //= primes[i]    
            times += 1
        if times > 0:
            res.append((primes[i], times))
        i += 1
    if n != 1:
        res.append((n, 1))
    return res    



primes = sieve(ceil(2 ** 15.5))
for line in stdin:
    n = int(line[:-1])
    pf = prime_factors(abs(n))
    res = []
    if n < 1: 
        res.append("-1")       
    res.extend(f"{a}^{b}" if b >= 2 else f"{a}" for a, b in pf)
    print(" ".join(res))



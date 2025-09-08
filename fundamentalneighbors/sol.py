from collections import Counter
import sys

def sieve(upto):
    primes = [True for i in range(upto + 1)]
    primes[0] = primes[1] = False
    p = 2
    while p * p <= upto:
        if primes[p]:
            for i in range(p * p, upto + 1, p):
                primes[i] = False
        p += 1
    return [i for i in range(2, upto + 1) if primes[i]]

def prime_factors(primes, n):
    og = n
    res = Counter()
    i = 0
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            n //= primes[i]
            res[primes[i]] += 1
        else:
            i += 1
    if n != 1:
        res[n] += 1
    #print(f"{og=},{res}")
    return res

def fundamental_neighbor(primes, n):
    res = 1
    for k, v in prime_factors(primes, n).items():
        res *= v ** k
    return res

primes = sieve(10 ** 5)

for line in sys.stdin:
    n = int(line[:-1])
    print(f"{n} {fundamental_neighbor(primes, n)}")
    

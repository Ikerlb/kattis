from collections import Counter

def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

def prime_factors(primes, n):
    res = Counter()
    i = 0
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            res[primes[i]] += 1
            n //= primes[i]
        else:
            i += 1
    if n != 1:
        res[n] += 1
    return res

primes = sieve(100_000)

n = int(input())
pfs = prime_factors(primes, n)
if len(pfs) == 1:
    print("yes")
else:
    print("no")

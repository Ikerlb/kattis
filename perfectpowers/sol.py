from collections import Counter
import fileinput
from math import gcd

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
for line in fileinput.input():
    n = int(line[:-1])
    if n == 0:
        break
    is_neg = n < 0
    n = abs(n)
    pfs = list(prime_factors(primes, n).items())
    div = gcd(*[b for _, b in pfs])
    # if n is negative
    # only odd powers
    # will work
    while is_neg and div % 2 == 0:
        div //= 2
    print(div)

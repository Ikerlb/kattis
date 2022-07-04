from math import ceil
from collections import Counter
from functools import lru_cache
from sys import stdin
#sys.stdin.buffer.read()

def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

@lru_cache(None)
def factors(n):
    nms = i = 0
    res = 1
    while n != 1 and i < len(primes):
        pw = 0
        while n % primes[i] == 0:
            pw += 1
            n //= primes[i]
        if pw != 0:
            res *= (1 + pw)
            nms += 1
        i += 1
    if n != 1:
        nms += 1
        res *= 2
    return res - nms

upto = ceil((10 ** 6) ** 0.5)
primes = sieve(upto)


n = int(input())
for _ in range(n):
    res = 1           
    print(factors(int(input())))

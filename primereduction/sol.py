import math
from sys import stdin

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
    i = res = 0
    while n != 1 and i < len(primes):
        while n % primes[i] == 0:
            n //= primes[i]    
            res += primes[i]
        i += 1
    if n != 1:
        res += n
    return res

primes = sieve(math.ceil(2 ** 15.5))
while True:
    n = int(input())
    if n == 4:
        break
    i = 1
    while True:
        nn = prime_factors(n)    
        if n == nn:
            print(nn, i)
            break
        n = nn
        i += 1

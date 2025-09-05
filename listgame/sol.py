from math import sqrt, ceil
import fileinput

def sieve(upto):
    primes = [True for _ in range(upto + 1)]
    primes[0] = primes[1] = False
    for i in range(2, ceil(sqrt(upto + 1))):
        if primes[i]:
            for j in range(i * i, upto + 1, i):
                primes[j] = False
    res = []
    for i in range(upto + 1):
        if primes[i]:
            res.append(i)
    return res
        
def prime_factors(n, primes):
    factors = []
    i = 0
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            n //= primes[i]
            factors.append(primes[i])
        else:
            i += 1
    if n != 1:
        factors.append(n)
    return factors

n = int("".join(fileinput.input()))
primes = sieve(10 ** 5)
print(len(prime_factors(n, primes)))

from sys import stdin
from math import ceil

def sieve(upto):
    not_primes = set()
    primes = []
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

def sum_divisors(n):
    i = 0
    res = 1
    while n != 1 and i < len(primes):  
        mult = primes[i]
        total = 1
        while n % primes[i] == 0:
            total += mult
            mult *= primes[i]
            n //= primes[i]
        i += 1
        res *= total
    return res

primes = sieve(ceil(2 ** 15.5))

for line in stdin:
    n = int(line[:-1])
    sd = sum_divisors(n)
    diff = abs(sd - 2 * n)
    if diff == 0:  
        print(f"{n} perfect")
    elif diff <= 2: 
        print(f"{n} almost perfect")
    else:
       print(f"{n} not perfect")

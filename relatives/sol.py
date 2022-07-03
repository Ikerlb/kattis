from math import ceil

def sieve(n):
    primes = []
    not_primes = set()
    for i in range(2, n + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, n + 1, i):
            not_primes.add(j)
    return primes

def phi(n):
    ans = n
    i = 0
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            ans -= ans // primes[i]
        while n % primes[i] == 0:
            n //= primes[i]
        i += 1
    if n != 1:
        ans -= ans // n
    return ans


primes = sieve(ceil(10 ** 4.5))
while True:
    n = int(input())
    if n == 0:
        break
    print(phi(n))

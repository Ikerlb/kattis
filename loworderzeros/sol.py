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

def prime_factors(n, primes, c):
    i = 0    
    while n != 1 and i < len(primes):
        while n % primes[i] == 0:
            n //= primes[i]
            c[primes[i]] += 1
        i += 1
    if n != 1:
        c[n] += 1
    return c

def low_order_digit(n, primes):
    i = 0    
    c = Counter()
    for i in range(2, n + 1):
        prime_factors(i, primes, c)        
    c[2] -= c[5]
    del c[5]
    res = 1
    for k, v in c.items(): 
        res = (res * (k ** v)) % 10
    return res


c = Counter()
res = 1
dp = [[1, 0, 0], [1, 0, 0]]
upto = (10 ** 6)
for i in range(2, upto + 1):
    c = dp[-1][:]
    while i % 2 == 0:
        i //= 2
        c[1] += 1
    while i % 5 == 0:
        i //= 5
        c[2] += 1
    c[0] = (i * c[0]) % 10
    dp.append(c)

while True:
    n = int(input())
    if n == 0:
        break
    others, eot, eof = dp[n]
    diff = eot - eof
    res = (others * (1 << diff)) % 10  
    print(res)

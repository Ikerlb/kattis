from sys import stdin

def sieve(upto):
    primes = [True for _ in range(upto + 1)]
    res = []
    for i in range(2, upto + 1):
        if primes[i]:
            res.append(i)
        for j in range(i * i, upto + 1, i):
            primes[j] = False
    return res
            
def prime_factors(n):
    i = 0    
    res = [0 for _ in range(len(primes))]
    while n != 1 and i < len(primes):
        while n % primes[i] == 0:
            n //= primes[i]
            res[i] += 1 
        i += 1
    return res

primes = sieve(431)

dp = [[0 for _ in range(len(primes))]]
for i in range(1, 432):
    cur = dp[-1][:]
    for i, p in enumerate(prime_factors(i)):
        cur[i] += p
    dp.append(cur)

for line in stdin:
    n, k = map(int, line[:-1].split(" "))
    res = dp[n][:]
    for i in range(len(primes)):
        res[i] -= min(res[i], dp[n - k][i] + dp[k][i])
    pres = 1
    for p in res:
        if p > 0:
            pres *= p + 1
    print(pres)

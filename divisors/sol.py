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
            
def prime_factors(n, res):
    i = 0    
    #res = [0 for _ in range(len(primes))]
    while n != 1 and i < len(primes):
        while n % primes[i] == 0:
            n //= primes[i]
            res[i] += 1 
        i += 1
    return res

primes = sieve(431)

dp = [[0 for _ in range(len(primes))] for _ in range(432)]
for i in range(1, 432):
    #for j, p in enumerate(prime_factors(i), ):
    for j in range(len(prime_factors(i, dp[i]))):
        dp[i][j] += dp[i - 1][j]

for line in stdin:
    n, k = map(int, line[:-1].split(" "))
    res = 1
    for i in range(len(primes)):
        res *= (dp[n][i] - min(dp[n][i], dp[n - k][i] + dp[k][i])) + 1
    #    res[i] -= min(res[i], dp[n - k][i] + dp[k][i])
    #for p in res:
    #    if p > 0:
    #        pres *= p + 1
    print(res)

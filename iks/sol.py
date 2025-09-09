import fileinput
from collections import Counter

ipt = fileinput.input()

n = int(next(ipt)[:-1])
l = list(map(int, next(ipt)[:-1].split(" ")))

def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)    
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

UPTO = 10000
primes = sieve(UPTO)

def prime_factors(primes, n):
    i = 0
    res = Counter()
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            res[primes[i]] += 1
            n //= primes[i]
        else:
            i += 1
    if n != 1:
        res[n] += 1
    return res

# 4 5 6 7 8
# 2 * 2
# 


def solve(primes, seq):
    cs = [prime_factors(primes, n) for n in seq]
    ca = Counter()
    for c in cs:
        ca.update(c)
    
    nc = Counter()
    gcd = 1
    for p, f in ca.items():
        d, m = divmod(f, len(seq))
        if d > 0:
            nc[p] = d
            gcd *= p ** d
            
    moves = 0
    for n, c in zip(seq, cs):
        for p, f in nc.items():
            if c[p] < f:
                moves += f - c[p]
    return gcd, moves
            
gcd, moves = solve(primes, l)
print(f"{gcd} {moves}")

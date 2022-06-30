def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

def is_prime(n):
    i = 0
    while i < len(primes) and primes[i] < n:
        if n % primes[i] == 0:
            return False
        i += 1
    return True

def _pow(n, k, mod):
    if k == 0:
        return 1
    half = _pow(n, k >> 1, mod) % mod
    if k & 1 == 0:
        return half * half % mod
    return (((half * half) % mod) * n) % mod

primes = sieve(32000)
while True:
    p, a = map(int, input().split(" "))
    if p == a == 0:
        break
    if not is_prime(p) and _pow(a, p, p) == a: 
        print("yes")
    else:
        print("no")

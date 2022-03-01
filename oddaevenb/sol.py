from functools import lru_cache

MOD = 10 ** 9 + 7

@lru_cache(None)
def A(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    return (B(n - 1) % MOD) + (A(n - 2) % MOD) % MOD

@lru_cache(None)
def B(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return ((B(n - 2) % MOD) + (A(n - 2) % MOD)) % MOD

n = int(input())
print((A(n) + B(n)) % MOD)

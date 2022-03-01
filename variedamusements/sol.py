from functools import lru_cache

#lru_cache(None)
#def A(n):
#    if n == 0:
#        return 1
#    cb = (b * B(n - 1)) % MOD
#    cc = (c * C(n - 1)) % MOD
#    return (cb + cc) % MOD

#lru_cache(None)
#def B(n):
#    if n == 0:
#        return 1
#    ca = (a * A(n - 1)) % MOD
#    cc = (c * C(n - 1)) % MOD
#    return (ca + cc) % MOD

#lru_cache(None)
#def C(n):
#    if n == 0:
#        return 1
#    ca = (a * A(n - 1)) % MOD
#    cb = (b * B(n - 1)) % MOD
#    return (ca + cb) % MOD

MOD = 10 ** 9 + 7
n, a, b, c = map(int, input().split(" "))

A = [1] * n
B = [1] * n
C = [1] * n

for i in range(1, n):
    A[i] = (((b * B[i - 1]) % MOD) + ((c * C[i - 1]) % MOD)) % MOD
    B[i] = (((a * A[i - 1]) % MOD) + ((c * C[i - 1]) % MOD)) % MOD
    C[i] = (((b * B[i - 1]) % MOD) + ((a * A[i - 1]) % MOD)) % MOD

ca = (a * A[n - 1]) % MOD
cb = (b * B[n - 1]) % MOD
cc = (c * C[n - 1]) % MOD

print((ca + cb + cc) % MOD)

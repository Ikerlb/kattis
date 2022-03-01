from functools import lru_cache

def A(n, a, b, c):
    if n == 0:
        return 1
    return b * B(n - 1, a, b, c) + c * C(n - 1, a, b, c)

def B(n, a, b, c):
    if n == 0:
        return 1
    return a * A(n - 1, a, b, c) + c * C(n - 1, a, b, c)

def C(n, a, b, c):
    if n == 0:
        return 1
    return a * A(n - 1, a, b, c) + b * B(n - 1, a, b, c)

n, a, b, c = map(int, input().split(" "))

ca = a * A(n - 1, a, b, c)
cb = b * B(n - 1, a, b, c)
cc = c * C(n - 1, a, b, c)

print(ca + cb + cc)

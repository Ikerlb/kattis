from math import isqrt
from functools import lru_cache

def digits(n):
    while n > 0:
        n, d = divmod(n, 10)
        yield d

def move(n):
    return sum(d * d for d in digits(n))

@lru_cache(None)
def is_happy(n):
    s = set()
    while n not in s and n != 1:
        s.add(n)
        n = move(n)
    return n == 1

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

tcs = int(input())
for _ in range(tcs):
    i, n = map(int, input().split(" "))
    res = "YES" if is_prime(n) and is_happy(n) else "NO"
    print(f"{i} {n} {res}")

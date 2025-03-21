import random

def mod_exp(base, exp, mod):
    """Efficient modular exponentiation: (base^exp) % mod."""
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def is_prime(n, k=10):
    """Miller-Rabin primality test for large numbers.
    
    - n: The number to test for primality.
    - k: Number of rounds (higher = more accurate).
    """
    if n < 2:
        return False
    if n in {2, 3, 5, 7, 11, 13, 17}:
        return True
    if n % 2 == 0:
        return False

    # Write n - 1 as d * 2^r
    d, r = n - 1, 0
    while d % 2 == 0:
        d //= 2
        r += 1

    # Perform k rounds of testing
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = mod_exp(a, d, n)

        if x == 1 or x == n - 1:
            continue

        is_composite = True
        for _ in range(r - 1):
            x = mod_exp(x, 2, n)
            if x == n - 1:
                is_composite = False
                break
        
        if is_composite:
            return False  # Definitely composite

    return True  # Probably prime

def solve(n):
    n = n - 3
    for fst in range(2, n):
        snd = n - fst
        if is_prime(fst, 3) and is_prime(snd, 3):
            return (3, fst, snd)
    return None

n = int(input())
print(" ".join(map(str, solve(n))))

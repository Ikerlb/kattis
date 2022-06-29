def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto, i):
            not_primes.add(j)
    return primes

upto = 40000
primes = sieve(upto)

def is_prime(n):
    i = 0    
    while i < len(primes) and primes[i] * primes[i] <= n:
        if n % primes[i] == 0:
            return False
        i += 1
    return True

# n is odd, obs
def find_prime_greater(n):
    while not is_prime(n):
        n += 2
    return n

while True:
    n = int(input())
    if n == 0:
        break
    # from 2 * n + 1 because 2 * n
    # always even
    gp = find_prime_greater(2 * n + 1)
    if is_prime(n):
        print(f"{gp}")    
    else:
        print(f"{gp} ({n} is not prime)")


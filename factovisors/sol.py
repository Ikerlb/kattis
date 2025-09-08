import fileinput
from collections import Counter

def is_prime(n):
    # Our list of deterministic bases
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    # Handle simple cases and check if n is one of our bases
    if n < 2:
        return False
    if n in bases:
        return True
    if any(n % b == 0 for b in bases): # Optimization for small factors
        return False

    # The single-base test function (our witness checker)
    def is_composite_witness(a, n):
        s = 0
        d = n - 1
        while d % 2 == 0:
            d >>= 1
            s += 1
        
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == 1:
                return True
            if x == n - 1:
                return False
        
        return True

    # Run the test for all our deterministic bases
    for a in bases:
        if is_composite_witness(a, n):
            return False
            
    return True

def sieve(upto):
    primes = []
    not_prime = set()
    for i in range(2, upto + 1):
        if i not in not_prime:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_prime.add(j)
    return primes

def prime_factors(primes, n):
    factors = Counter()
    i = 0
    while n != 1 and i < len(primes):
        if n % primes[i] == 0:
            factors[primes[i]] += 1
            n //= primes[i]
        else:
            i += 1
    if n != 1:
        factors[n] += 1
    return factors
        

# legendre's formula
def largest_power(n, p): 
    res = 0 

    # Calculate res = n/p + n/(p^2) + n/(p^3) + .... 
    while n > 0: 
        n //= p 
        res += n 
    return res

def divides_fact(n, m, primes):
    if m <= n:
        return True
    if is_prime(m):
        return False
    for k, v in prime_factors(primes, m).items():
        if not largest_power(n, k) >= v:
            return False
    return True

primes = sieve(10 ** 6)

for line in fileinput.input():
    n, m = map(int, line[:-1].split(" "))
    if m != 0 and divides_fact(n, m, primes):
        res = "divides"
    else:
        res = "does not divide"
    print(f"{m} {res} {n}!")    
    #print(f"pfs of {m=} is pf={prime_factors(primes, m)}")


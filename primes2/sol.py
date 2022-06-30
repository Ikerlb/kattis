t = int(input())

def convert(n, bases):
    res = set()
    for b in bases:
        try:
            nn = int(n, b)
            res.add(nn)
        except:
            continue    
    return res

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lowest_terms(a, b):
    d = gcd(a % b, b)
    return f"{a//d}/{b//d}"
    
def is_prime(n, primes):
    for p in primes:
        if n != p and n % p == 0:
            return False
        if p > n:
            break
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

primes = sieve(2000000)

for _ in range(t):
    s = input()
    st = convert(s, [2, 8, 10, 16])
    n = len(st)
    p = sum(1 for nn in st if is_prime(nn, primes))
    print(lowest_terms(p, n)) 



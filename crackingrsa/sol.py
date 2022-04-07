def sieve(upto):
    not_primes = set()    
    for i in range(2, upto):
        if i in not_primes: 
            continue
        yield i
        for j in range(i * i, upto, i):    
            not_primes.add(j)

primes = list(sieve(1000))


def find_factors(n, primes):
    for p in primes:
        for q in primes:
            if p * q == n:
                return p, q
    return None


# φ(n) = (p - 1) * (q - 1)
def totient(p, q):
    return (p - 1) * (q - 1)

def euclid(a, b): 
    # Base Case 
    if a == 0 :  
        return b,0,1
             
    gcd, x1, y1 = euclid(b%a, a) 
     
    x = y1 - (b//a) * x1 
    y = x1 
     
    return gcd, x, y


tcs = int(input())
for _ in range(tcs):
    n, e = map(int, input().split(" "))
    p, q = find_factors(n, primes)
    tot = totient(p, q)
    gcd, x, y = euclid(e, tot)
    assert(gcd == 1)
    print(x % tot)


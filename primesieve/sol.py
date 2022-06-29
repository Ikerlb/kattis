#def sieve(upto):
#    primes = []            
#    not_primes = set()
#    for i in range(2, upto):
#        if i not in not_primes:
#            primes.append(i)
#        for j in range(i * i, upto, i):
#            not_primes.add(j)
#    return primes

def sieve(upto):
    primes = [True for _ in range(upto)]
    primes[0] = primes[1] = False
    for i in range(2, upto):
        for j in range(i * i, upto, i):
            primes[j] = False
    return primes

primes = sieve(10 ** 7)
print(len(primes))

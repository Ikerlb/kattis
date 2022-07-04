def sieve(upto):
    primes = []
    not_primes = set()
    for i in range(2, upto + 1):
        if i not in not_primes:
            primes.append(i)
        for j in range(i * i, upto + 1, i):
            not_primes.add(j)
    return primes

def phi(n):
    i = 0                    
    res = n
    while i < len(primes) and primes[i] * primes[i] <= n:
        if n % primes[i] == 0:
            res -= (res // primes[i]) 
        while n % primes[i] == 0:
            n //= primes[i]
        i += 1
    if n != 1:
        res -= res // n
    return res



# 0/1
# 1/1

# 1/2

# 1/3
# 2/3

# 1/4
# 3/4

# 1/5
# 2/5
# 3/5
# 4/5

# 1/6
# 5/6

primes = sieve(100)
ps = [1]
upto = 10000
for i in range(1, upto + 1): 
    ps.append(ps[-1] + phi(i))    


n = int(input())
for _ in range(n):
    i, n = map(int, input().split(" "))
    print(i, ps[n])

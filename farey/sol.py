import fileinput

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


# note, I went back to this 
# and had no clue what this 
# did.
# so i'll leave some notes for
# future iker
# the reason why we have a prefix sum
# is that if N is 1
# the only fractions we have are 

# 0/1
# 1/1

# if we have N=2, we have all the fractions 
# for N - 1 and also the number of i < N
# such that i and N are relative primes (GCD(i, N) == 1)
# which is coincidentally what euler's phi
# functions does

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

inpt = fileinput.input()
n = int(next(inpt)[:-1])
for _, line in zip(range(n), inpt):
    i, n = map(int, line[:-1].split(" "))
    print(i, ps[n])

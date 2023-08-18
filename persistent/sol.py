from sys import stdin
from math import isqrt

#def divisors(n):
#    for i in range(2, isqrt(n) + 1):
#        d, m = divmod(n, i)
#        if m == 0 and :
#            yield d, i

def reduce(c):
    

def solve(n):
    if n < 10:
        return f"1{n}"
    res = []
    while n != 1:
        for i in range(2, 10):
            if n % i == 0:
                res.append(i)
                n //= i
        else: # couldn't divide by any digits, it must be impossible
            break
    
    return "".join(map(lambda x: str(x), reversed(res)))

#for line in stdin:
#    if line == "-1":
#        continue
#    n = int(line[:-1])


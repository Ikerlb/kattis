from functools import lru_cache
from math import inf

# TODO: i think i can do this greedily
# without recursive overhead and dp array
# overhead
#def solve(a, b, m, n):
#    def dp(target):
#        if target < m:
#            return inf
#        if target == m:    
#            return 0
#        return min(a + dp(target - 1), b + dp(target >> 1))
#    return dp(n)

#def solve(res, a, b, m, n):
#    for i in range(m, n + 1):
#        res[i] = inf    
#    res[m] = 0
#    for i in range(m + 1, n + 1):
#        if i - 1 >= m:
#            res[i] = min(res[i], a + res[i - 1])
#        if i >> 1 >= m:
#            res[i] = min(res[i], b + res[i >> 1]) 
#    return res[n]    

def solve(a, b, n, m):
    res = 0
    while n > m:
        # calculate price per unit            
        # but only if halfing is 
        # still greater or equal
        # than m
        if (n >> 1) >= m:
            ppub = b / (n - (n >> 1))
            if ppub <= a:
                res += b
                n = n >> 1    
            else:
                n -= 1
                res += a
        else:
            res += (n - m) * a     
            break
    return res
        


tcs = int(input())
for tc in range(tcs):
    n, m, l = map(int, input().split(" "))
    res = []
    for _ in range(l):
        agency, rest = input().split(":")
        a, b = map(int, rest.split(","))
        res.append((solve(a, b, n, m), agency))
    res.sort() 
    print(f"Case {tc + 1}")
    for cost, agency in res:
        print(f"{agency} {cost}")

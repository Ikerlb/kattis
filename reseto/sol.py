def sieve(upto, k):
    p = [True for _ in range(upto + 1)]
    res = 0
    for i in range(2, upto + 1):
        for j in range(i, upto + 1, i):    
            if p[j]:
                p[j] = False
                res += 1
            if res == k:
                return j

n, k = map(int, input().split(" "))
print(sieve(n, k))

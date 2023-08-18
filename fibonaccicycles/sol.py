#def _next(p1, p2, k):
#    return p2, (p1 + p2) % k
def _next(p1, p2, k):
    return (p1 + p2) % k

def solve(k):
    s = {}
    p1 = p2 = 1
    i = 2
    while (n := _next(p1, p2, k)) not in s:
        s[n] = i
        p1, p2 = p2, n
        i += 1
    return s[n]

tcs = int(input())
queries = [int(input()) for _ in range(tcs)]

for k in queries:
    print(solve(k))

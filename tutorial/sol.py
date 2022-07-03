from math import log

def fact(n, m):
    res = 1
    for i in reversed(range(1, n + 1)):
        res *= i
        if res > m:
            return False
    return True

def po2(n, m):
    res = 1
    for i in range(n):
        res *= 2
        if res > m:
            return False
    return True
        

def nlogn(n, m):
    return log(n, 2) * n <= m

d = {
    1: fact,
    2: po2,
    3: lambda n, m: n ** 4 <= m,
    4: lambda n, m: n ** 3 <= m,
    5: lambda n, m: n ** 2 <= m,
    6: nlogn,
    7: lambda n, m: n <= m
}

m, n, t = map(int, input().split(" "))

if d[t](n, m):
    print("AC")
else:
    print("TLE")

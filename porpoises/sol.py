def prod(m1, m2, mod):
    return [[sum((a*b) % mod for a,b in zip(X_row,Y_col)) % mod for Y_col in zip(*m2)] for X_row in m1]

def identity(n):
    m = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        m[i][i] = 1
    return m

def pow(m, k, mod):
    if k == 1:
        return m
    if k % 2 == 0:
        h = pow(m, k >> 1, mod)
        return prod(h, h, mod)
    h = pow(m, k >> 1, mod)
    return prod(m, prod(h, h, mod), mod)

def fibo(n, mod):
    m = [
        [0, 1],
        [1, 1]
    ]
    v = [
        [1],
        [1]
    ]
    if n == 0:
        return v[0][0]
    return prod(pow(m, n, mod), v, mod)[0][0]

tcs = int(input())
for _ in range(tcs):
    i, n = map(int, input().split(" "))
    print(i, fibo(n - 1, 10 ** 9))

def prod(X, Y, mod):
    return [[sum((a*b) % mod for a,b in zip(X_row,Y_col)) % mod for Y_col in zip(*Y)] for X_row in X]

def _pow(m, k, mod):
    if k == 1:
        return m
    elif k % 2 == 0:
        half = _pow(m, k >> 1, mod)
        return prod(half, half, mod)
    else:
        half = _pow(m, k >> 1, mod)
        return prod(half, prod(half, m, mod), mod)

def solve(rm, k, mod, init):
    matrix = _pow(rm, k, mod)
    return prod(matrix, init, mod)


def build_matrix(n, rec):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    matrix[0][0] = 1 
    matrix[1][:] = rec

    for i in range(2, n):
        matrix[i][i - 1] = 1
    return matrix

n = int(input())
rec = list(map(int, input().split(" ")))
matrix = build_matrix(n + 1, rec)

v = [[int(i)] for i in input().split(" ")] + [[1]]
v.reverse()

qs = int(input())
for _ in range(qs):
    qn, mod = map(int, input().split(" "))
    print(solve(matrix, qn, mod, v)[-1][0])

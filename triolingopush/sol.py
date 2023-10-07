# n = 3
# 1 0 0 | 1     1+0+0   1
# 0 0 1 | 1  => 0+0+2 = 2
# 1 1 1 | 2     1+1+2   4

# n = 4
# 1 0 0 | 1     1+0+0   1
# 0 0 1 | 2  => 0+0+4 = 4
# 1 1 1 | 4     1+2+4   7


def prod(A, B, M):
    return [[sum((a * b) % M for a,b in zip(A_row, B_col)) % M for B_col in zip(*B)] for A_row in A]

# to avoid creating the diagonal matrix
# just make base case equal to 1
def mat_pow(m, k, mod):
    if k == 1:
        return m
    elif k % 2 == 0:
        half = mat_pow(m, k >> 1, mod)
        return prod(half, half, mod)
    else:
        half = mat_pow(m, k >> 1, mod)
        return prod(prod(half, half, mod), m, mod)

def solve(n):
    if n <= 2:
        return n

    m = [[1,0,0],[0,0,1], [1,1,1]]
    mod = 10 ** 9 + 7
    v = [[1], [1], [2]]
    mpow = mat_pow(m, n - 2, mod)

    return prod(mpow, v, mod)[-1][0]

n = int(input())
print(solve(n))

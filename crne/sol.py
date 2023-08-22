def solve(n):
    m = (n >> 1) + 1
    if n % 2 == 0:
        return m * m
    return m * m + m

print(solve(int(input())))

from math import sqrt, floor

n = int(input())
tcs = [int(input()) for _ in range(n)]

def gauss(i):
    return (i * (i + 1)) >> 1

# first i such that
# (n - gauss(i))
# is divisible
# by i
def solve(n):
    i = 2
    while n >= (g := gauss(i)):
        if ((n - g) % i) == 0:
            return i
        i += 1

def format_solution(n, m):
    start = gauss(m)
    offset = (n - start) // m + 1
    return f'{n} = {" + ".join(map(str, range(offset, offset + m)))}'

for n in tcs: 
    if (s := solve(n)) is not None:
        print(format_solution(n, s))
    else:
        print("IMPOSSIBLE")

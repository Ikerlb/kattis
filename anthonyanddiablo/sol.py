from decimal import Decimal, getcontext

A, N = map(Decimal, input().split(" "))

# shamelessly stolen from 
# https://docs.python.org/3/library/decimal.html
def pi():
    getcontext().prec += 2  # extra digits for intermediate steps
    three = Decimal(3)      # substitute "three=3.0" for regular floats
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n+na, na+8
        d, da = d+da, da+32
        t = (t * n) / d
        s += t
    getcontext().prec -= 2
    return +s

# isoperimetric inequality
max_area = (N * N) / (Decimal(4) * pi())

if A <= max_area:
    print("Diablo is happy!")
else:
    print("Need more materials!")

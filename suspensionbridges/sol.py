from decimal import getcontext, Decimal

# takes in decimal
def sinh(x):
    return (x.exp() - (-x).exp()) / Decimal(2)

# takes in decimal
def cosh(x):
    return (x.exp() + (-x).exp()) / Decimal(2)

d, s = map(lambda x: Decimal(x), input().split(" "))

def _try(a, d, s):
    return a * cosh(d/(2*a)) - a - s

# we don't quite know the limit
# so to keep it 'safe' we do
# galloping search
def galloping_search(d, s):
    l, r = Decimal(0), Decimal(1)
    while _try(r, d, s) > 0: 
        l, r = r, r * 2
    m = None
    eps = Decimal(0.0000000000001)
    while abs(r - l) > eps:
        m = (l + r) / 2
        if _try(m, d, s) > 0:
            l = m
        else:
            r = m
    return m

def l(a, s):
    return 2*a * sinh(d / (2 * a))

getcontext().prec = 20
a = galloping_search(d, s)
print(l(a, s))

a, b, c, d = map(int, input().split(" "))

def lcm(a, b):
    return (a * b) // gcd(a, b)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

div = lcm(c, d)
print((b // div) - ((a - 1) // div))

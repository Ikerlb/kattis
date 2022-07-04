def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def simplify(a, b):
    d = gcd(a, b)
    return f"{a // d}/{b // d}"

n = int(input())
rings = list(map(int, input().split(" ")))
first = rings[0]
print("\n".join(simplify(first, x) for x in rings[1:]))

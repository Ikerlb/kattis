a, b = map(int, input().split())

def pow(a, b, m):
    if b == 0:
        return 1
    if b % 2 == 0:
        h = pow(a, b >> 1, m)
        return (h * h) % m
    else:
        h = pow(a, b >> 1, m)
        return (((h * h) % m) * a) % m

# took me eons to figure out
# all the terms cancel out
# on both ends because of the % a

if a % 2 == 1:
    print(0) # cancel the last and the rest will cancel each other % a
else:
    print(pow(a >> 1, b, a)) # can't match the middle % a

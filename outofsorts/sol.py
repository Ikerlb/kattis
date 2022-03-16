n, m, a, c, x0 = map(int, input().split(" "))

def generate(n, m, a, c, x0):
    x = [0] * n
    prev = x0
    for i in range(n):
        x[i] = (a * prev + c) % m
        prev = x[i]
    return x

# we just do the binary search!
def bs(x, target):
    l, r = 0, len(x) - 1
    while l <= r:
        m = (l + r) >> 1
        if x[m] == target:
            return True
        elif x[m] < target:
            l = m + 1
        else:    
            r = m - 1
    return False

x = generate(n, m, a, c, x0)

print(sum(1 for n in x if bs(x, n)))

from sys import stdin

def _pow(a, k, mod):
    if k == 0:
        return 1
    if k % 2 == 0:
        h = _pow(a, k >> 1, mod)
        return (h * h) % mod
    h = _pow(a, k >> 1, mod)
    return (a * h * h) % mod

def _eval(a, op, b):
    if op == "+":
        return a + b
    if op == "*":
        return a * b
    if op == "^":
        return _pow(a, b, 10000)

for line in stdin:
    a, op, b = line[:-1].split(" ")
    s = str(_eval(int(a), op, int(b)))
    print(int(s[-4:]))

import sys

N = int(sys.stdin.readline())

turtle = "GABBY"
hare = "SPIKE"

d = {}
d[turtle] = N
d[hare] = N

def _next(char):
    d[char] -= 1
    sys.stdout.write(f"NEXT {char}\n")
    sys.stdout.flush()
    s, e = map(int, sys.stdin.readline().split(" "))
    if s == 0 or d[char] == 0:
        sys.stdout.write(f"ASK {char}\n")
        sys.stdout.flush()
        sys.exit()
    return e != 0

# get k*lambda
kl = 0
e = False
while not e:
    e = _next(turtle)
    e = _next(hare) 
    e = _next(hare)
    kl += 1

# get lambda
lamb = 0
e = False 
while not e:
    lamb += 1
    e = _next(turtle)

n = (N - kl) % lamb
for _ in range(n):
    _next(turtle)

sys.stdout.write(f"ASK {turtle}\n")
sys.stdout.flush()

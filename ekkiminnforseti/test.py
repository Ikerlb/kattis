from string import ascii_lowercase
from random import choice, shuffle

def random_string(size):
    return "".join(choice(ascii_lowercase) for _ in range(size))

def random_ordering(m):
    l = [i + 1 for i in range(m)]
    shuffle(l)
    return l

N = 10000
M = 2000
#N = 10
#M = 2
NAME_SIZE = 20

candidates = [random_string(NAME_SIZE) for _ in range(M)]
votes = [random_ordering(M) for _ in range(N)]

print(N, M)
print("\n".join(candidates))
print("\n".join(" ".join(map(str, order)) for order in votes))

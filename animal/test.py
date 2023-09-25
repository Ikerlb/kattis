from random import shuffle
import sys

sys.setrecursionlimit(1000000)


n = 100000
l = list(range(1, n + 1))

shuffle(l)


while len(l) > 1:
    rite = l.pop()
    left = l.pop()
    tup = [left, rite]
    l.append(tup)

print(l)

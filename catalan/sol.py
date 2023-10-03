from sys import stdin
from decimal import *

MAX = 5001

catalan = [1 for _ in range(MAX)]
for i in range(MAX - 1):
    catalan[i + 1] = ((4 * i + 2) * catalan[i]) // (i + 2)

#print(catalan)

qs = next(stdin)

for line in stdin:
    n = int(line[:-1])
    print(int(catalan[n]))


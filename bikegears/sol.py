from decimal import *

getcontext().prec = 20

f, b = map(int, input().split(" "))

front = [int(c) for c in input().split(" ")]
back = [int(c) for c in input().split(" ")]

arr = [(Decimal(f) / Decimal(b), f, b) for f in front for b in back]
arr.sort()

for _, f, b in arr:
    print(f"({f},{b})")

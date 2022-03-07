from collections import defaultdict
from math import inf
from bisect import bisect_left

n = int(input())
d = defaultdict(list)

k = int(input())

for _ in range(k):
    si, item = input().split(" ")
    d[item].append(int(si))

for k in d:
    d[k].sort()

m = int(input())
items = [input() for _ in range(m)]

def binary_search(arr, tar):
    l, r = 0, len(arr) - 1
    res = -1
    while l <= r:
        m = (l + r) >> 1
        if arr[m] <= tar:
            res = m
            l = m + 1
        else:
            r = m - 1
    return res

def solve(d, items):
    prev = 0
    res = []
    for n in items:
        idx = bisect_left(d[n], prev)
        if idx >= len(d[n]):
            return "impossible"
        else:
            prev = d[n][idx]
            res.append(prev)
    return res 

def solve_backwards(d, items):
    prev = inf
    res = []
    for n in reversed(items): 
        idx = binary_search(d[n], prev)
        if idx == -1:
            return "unique"
        else:
            prev = d[n][idx]
            res.append(prev) 
    return res

r1 = solve(d, items)
if r1 == "impossible":
    print(r1)    
else:
    r2 = solve_backwards(d, items)
    r2.reverse()
    if r2 == r1:
        print("unique")
    else:
        print("ambiguous")

from collections import deque
from functools import lru_cache
import math
from sys import stdin

# 1.in
# 
#    ##          ##
#    ##          ##
#    ##       ## ##
#    ##       ## ##
#    ##       ## ##
#    ##       ## ##
#    ## ##    ## ##
#    ## ##    ## ##
#    ## ## ## ## ##
#    ## ## ## ## ##

def neighbors(i, heights, n2l, n2r, res):
    if n2l[i] is None and n2r[i] is None:
        return
    if n2l[i] is not None:
        yield n2l[i]
    if n2r[i] is not None:
        yield n2r[i]

def calc_next(heights, reverse = False):
    s = []
    range_gen = range(len(heights))
    res = [None for _ in range(len(heights))]
    if reverse:
        range_gen = reversed(range_gen)
    for i in range_gen:
        n = heights[i]
        while s and heights[s[-1]] < n:
            res[s.pop()] = i
        s.append(i)    
    return res

@lru_cache(None)
def dp(i):
    if i < 0 or i >= len(heights):
        return math.inf
    if n2r[i] is None and n2l[i] is None:
        return 0
    res = math.inf
    if n2r[i] is not None:
        res = min(res, dp(n2r[i]) + 1)
    if n2l[i] is not None:
        res = min(res, dp(n2l[i]) + 1)
    return res

#n = int(input())
#heights = [int(input()) for _ in range(n)]
#if heights:
#    n2r = calc_next(heights)
#    n2l = calc_next(heights, reverse = True)
#    res = [str(dp(i)) for i in range(n)]
#    print(" ".join(res))

for i, line in enumerate(stdin):
    line = line[:-1]
    if i == 0:
        heights = [0 for _ in range(int(line))]
    else:
        heights[i - 1] = int(line)

n2r = calc_next(heights)
n2l = calc_next(heights, reverse = True)
res = [str(dp(i)) for i in range(len(heights))]
print(" ".join(res))

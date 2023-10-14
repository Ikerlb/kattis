from math import inf
from functools import lru_cache

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


tcs = int(input())

for _ in range(tcs):
    n, m = map(int, input().split(" "))
    sr, sc = map(int, input().split(" "))
    num = int(input())

    beepers = [(sr, sc)]
    beepers.extend(list(map(int, input().split(" "))) for _ in range(num))

    @lru_cache(None)
    def dp(used, cur):
        if used == (1 << (len(beepers))) - 1:
            return manhattan(beepers[cur], beepers[0])
        res = inf
        for i in range(len(beepers)):
            if (used >> i) & 1 == 0:
                cost = manhattan(beepers[i], beepers[cur])
                res = min(res, dp(used | (1 << i), i) + cost)
        return res

    print(dp(1, 0))

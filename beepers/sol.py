from itertools import permutations

def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def cost(beepers, perm, start):
    res = manhattan(start, beepers[perm[0]])
    for i in range(1, len(perm)):
        res += manhattan(beepers[perm[i - 1]], beepers[perm[i]])
    return res + manhattan(beepers[perm[-1]], start)

perms = [list(permutations(list(range(i)))) for i in range(11)]

tcs = int(input())

for _ in range(tcs):
    n, m = map(int, input().split(" "))
    sr, sc = map(int, input().split(" "))
    num = int(input())

    beepers = [list(map(int, input().split(" "))) for _ in range(num)]

    print(min(cost(beepers, p, (sr, sc)) for p in perms[num]))

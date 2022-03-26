def solve(s, e, d):
    return max(((e - s) // d) + 1, 0)

l, d, n = map(int, input().split(" "))

if l <= 12:
    print(0)
else:
    birds = [(0, 6), (l - 6, l)]
    for _ in range(n):
        m = int(input())
        birds.append((max(0, m - d), min(m + d, l)))

    birds.sort()

    ps, pe = birds[0]
    res = 0

    for s, e in birds[1:]:
        res += solve(pe, s, d)
        ps, pe = s, e
    print(res)

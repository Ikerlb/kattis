def _try(m, cities):
    return sum((n // m) + (n % m > 0) for n in cities)

for i in range(3):
    ncities, ballots = map(int, input().split(" "))
    if ncities == ballots == -1:
        break
    cities = [int(input()) for _ in range(ncities)]
    l, r = 0, max(cities) 
    res = r
    while l <= r: 
        m = (l + r) >> 1
        if _try(m, cities) <= ballots:
            r = m - 1
            res = m
        else:
            l = m + 1
    input() # burn empty line
    print(res)

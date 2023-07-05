from collections import defaultdict

fibos = [1, 1]

while fibos[-1] <= 10 ** 18:
    fibos.append(fibos[-2] + fibos[-1])

dfibos = {f:i for i, f in enumerate(fibos)}

n, m = map(int, input().split(" "))

heights = [int(s) for s in input().split(" ")]

g = defaultdict(list)

def dfs(g, n, dp):
    dp[n] = -1
    res = 1
    for nn in g[n]:
        if nn not in dp:
            res = max(res, 1 + dfs(g, nn, dp))
        elif nn in dp and dp[nn] != -1:
            res = max(res, 1 + dp[nn])
    dp[n] = res
    return res

for _ in range(m):
    s, t = map(lambda x: int(x) - 1, input().split(" "))
    hs = heights[s]
    ht = heights[t]

    if ht < hs:
        s, t = t, s
        hs, ht = ht, hs

    if not hs in dfibos: 
        continue
    if not ht in dfibos:
        continue
    if ht == hs == 1:
        g[s].append(t)
        g[t].append(s)
    elif dfibos[ht] - dfibos[hs] == 1:
        g[s].append(t)

if not g and any(h in dfibos for h in heights):
    print(1)
    exit()
elif not g:
    print(0)
    exit()

dp = {}
indices = sorted(range(len(heights)), key = lambda x: heights[x])


for i in indices:
    if heights[i] != 1:
        dfs(g, i, dp)

print(max(dp.values()))

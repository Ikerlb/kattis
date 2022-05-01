from collections import defaultdict, deque

# n is the number of countries
# ps is the number of trade partnerships
# c is the number of your country
# l is the number of the country that leaves
n, ps, c, l = map(int, input().split(" "))

c -= 1
l -= 1

g = defaultdict(set)

for _ in range(ps):
    s, t = map(int, input().split(" "))
    s -= 1
    t -= 1
    g[s].add(t)
    g[t].add(s)

q = deque([l])

visited = {i:len(g[i]) for i in range(n)}

while q:
    n = q.popleft()    
    #print(f"{n=}", f"{visited=}", f"{g=}", end= "\n\n")
    for nn in g[n]:
        g[nn].discard(n)    
        if len(g[nn]) <= visited[nn] // 2:
            q.append(nn)     

    if n in g and n in visited:
        del g[n]
        del visited[n]

print("stay" if c in visited else "leave")

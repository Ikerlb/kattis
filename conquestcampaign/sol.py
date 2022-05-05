from collections import deque

n, m, w = map(int, input().split(" "))
q = deque()
s = set()
for _ in range(w):
    r, c = map(lambda x: int(x) - 1, input().split(" "))    
    if (r, c) not in s: 
        q.append((r, c))
        s.add((r, c))

def neighbors(n, m, r, c):
    for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        if 0 <= r + dr < n and 0 <= c + dc < m:
            yield r + dr, c + dc

res = 0
while q:
    res += 1
    for _ in range(len(q)):
        r, c = q.popleft()
        for nr, nc in neighbors(n, m, r, c):
            if (nr, nc) not in s:    
                s.add((nr, nc))
                q.append((nr, nc))
print(res)

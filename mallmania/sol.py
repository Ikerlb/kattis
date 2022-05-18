from collections import deque

def solve(q, visited, m1):
    res = 0
    deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while q: 
        for _ in range(len(q)):
            r, c = q.popleft()
            if (r, c) in m1:
                return res
            for dr, dc in deltas:
                nr, nc = r + dr, c + dc
                tup = (nr, nc)
                if nr >= 0 and nc >= 0 and tup not in visited:
                    visited.add(tup)
                    q.append(tup)
        res += 1
    return -1


while True:
    p1 = int(input())
    if p1 == 0:
        break
    p1l = list(map(int, input().split(" ")))
    m1 = set()
    for i in range(0, len(p1l), 2):
        m1.add((p1l[i], p1l[i + 1]))
    p2 = int(input())
    p2l = list(map(int, input().split(" ")))
    visited = set()
    q = deque()
    for i in range(0, len(p2l), 2): 
        tup = (p2l[i], p2l[i + 1])
        visited.add(tup)
        q.append(tup)
    print(solve(q, visited, m1))

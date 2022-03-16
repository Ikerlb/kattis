from collections import deque

def solve(n):
    q = deque()
    for i in range(n, 0, -1):
        q.appendleft(i)
        q.rotate(i)
    return list(q)

tc = int(input())
for _ in range(tc):
    n = int(input())
    print(" ".join(map(str, solve(n))))

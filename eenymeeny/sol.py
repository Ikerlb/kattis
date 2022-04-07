from collections import deque

mod = len(input().split(" ")) - 1
n = int(input())
names = [input() for _ in range(n)]

q = deque(names)
teams = [[], []]
i = 0
while q:
    q.rotate(-mod)
    teams[i].append(q.popleft())
    i = 1 - i    

for t in teams:
    print(len(t))
    print("\n".join(t))


from collections import deque

_ = input()
q = deque((i + 1, int(s)) for i, s in enumerate(input().split(" ")))


#print(q)
#_, n = q[0]
#q.rotate((-n + 1) % len(q))
#print(q)

while q:
    i, n = q[0]
    q.rotate((1 - n) % len(q))
    q.popleft()
print(i)

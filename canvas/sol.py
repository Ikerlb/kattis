from heapq import heappush, heappop, heapify

tcs = int(input())

for _ in range(tcs):
    n = int(input())
    h = [int(m) for m in input().split(" ")]
    heapify(h) 
    total = 0
    while len(h) >= 2:
        t = heappop(h) + heappop(h)
        total += t
        heappush(h, t)
    print(total)

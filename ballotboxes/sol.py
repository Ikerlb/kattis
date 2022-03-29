from heapq import heappush, heappop
from math import ceil

# initially, we will do
# it in O(logn * b)
# we will see how it goes
# from there

for _ in range(3):
    n, b = map(int, input().split(" "))
    if n == b == -1:
        break
    h = []
    for _ in range(n):
        b -= 1
        pop = int(input())
        heappush(h, (-pop, pop, 1))
    for _ in range(b): 
        # i want to try two things

        # first to greedily assign
        # one more ballot to the 
        # city with the biggest ratio
        # of people / ballot

        # lets try that
        _, pop, cb = heappop(h) 
        d, m = divmod(pop, cb + 1)
        heappush(h, (- d - int(m > 0), pop, cb + 1))
    print(-h[0][0])
    input() # burn empty line

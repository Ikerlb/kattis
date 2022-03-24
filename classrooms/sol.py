from heapq import heappush, heappop

n, k = map(int, input().split(" "))
intervals = []
for _ in range(n):
    s, e = map(int, input().split(" "))    
    intervals.append((s, e))

intervals.sort()
print(intervals)

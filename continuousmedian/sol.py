from heapq import heappush, heappop

class Stream:
    def __init__(self):
        self.hi = []
        self.lo = []

    def _rebalance(self):
        if len(self.lo) > len(self.hi) + 1:
            n = -heappop(self.lo)
            heappush(self.hi, n) 
        while self.hi and self.hi[0] < -self.lo[0]:
            n1 = heappop(self.hi)
            n2 = heappop(self.lo) 
            heappush(self.lo, -n1)
            heappush(self.hi, n2)

    def add(self, n): 
        heappush(self.lo, -n)
        self._rebalance()

    def __repr__(self):
        return f"low: {self.lo}, hi: {self.hi}, {self.get_median()}"

    def get_median(self):
        if len(self.lo) == len(self.hi):
            return (-self.lo[0] + self.hi[0]) >> 1
        return -self.lo[0]


tcs = int(input())
for _ in range(tcs):
    n = int(input())    
    arr = list(map(int, input().split(" ")))
    s = Stream()
    res = 0
    for n in arr:
        s.add(n)
        res += s.get_median()
        #print(s)
    print(res)
